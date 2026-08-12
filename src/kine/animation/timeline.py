import os
import sys
import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Включаем классическую математическую типографику LaTeX (Computer Modern)
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'


class Timeline:
    """Менеджер анимаций Kine: генерация MP4 с настоящим LaTeX-шрифтом."""

    def __init__(self):
        self.fps = 60
        self.resolution = (1920, 1080)
        self.output_path = "output.mp4"
        self.video_writer = None
        self.current_obj = None

    def setup(self, fps: int, resolution: tuple, output_path: str):
        self.fps = fps
        self.resolution = resolution
        self.output_path = output_path

        w, h = self.resolution
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(self.output_path, fourcc, self.fps, (w, h))

    def _render_latex_frame(self, latex_text: str) -> np.ndarray:
        """Отрисовывает математику в стиле Computer Modern TeX."""
        w, h = self.resolution
        dpi = 100
        fig_w, fig_h = w / dpi, h / dpi

        # ФИКС: Масштабируем размер шрифта пропорционально высоте экрана.
        # Базовый размер 48pt рассчитан под 1080p и идеально масштабируется для 480p, 720p и 4K.
        scale_factor = h / 1080.0
        dynamic_fontsize = max(12, int(48 * scale_factor))

        fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
        fig.patch.set_facecolor('#0D0E15')
        ax.set_facecolor('#0D0E15')

        # Чистим от внешних долларов и автоматизируем TeX-операторы
        clean_body = latex_text.strip().replace('$', '')
        
        # Гарантируем, что тригонометрия пишется как TeX-команды \sin и \cos
        if '\\sin' not in clean_body:
            clean_body = clean_body.replace('sin', r'\sin')
        if '\\cos' not in clean_body:
            clean_body = clean_body.replace('cos', r'\cos')

        clean_latex = f"${clean_body}$"

        ax.text(
            0.5, 0.5, clean_latex,
            color='#39FF14',
            fontsize=dynamic_fontsize,
            ha='center',
            va='center',
            transform=ax.transAxes
        )
        ax.axis('off')

        fig.canvas.draw()
        buf = np.asarray(fig.canvas.buffer_rgba())
        plt.close(fig)

        frame = cv2.cvtColor(buf, cv2.COLOR_RGBA2BGR)

        # Устраняем погрешность округления Matplotlib
        if frame.shape[1] != w or frame.shape[0] != h:
            frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_AREA)

        return frame

    def reveal(self, obj, duration_seconds: float = 1.0):
        self.current_obj = obj
        total_frames = int(self.fps * duration_seconds)
        print(f"✨ [Timeline] Генерация Reveal ({duration_seconds}s, {total_frames} кадров MP4)...")

        latex_str = obj.to_latex() if hasattr(obj, "to_latex") else str(obj)
        frame = self._render_latex_frame(latex_str)

        for _ in range(total_frames):
            if self.video_writer:
                self.video_writer.write(frame)

    def hold(self, duration_seconds: float = 1.0):
        total_frames = int(self.fps * duration_seconds)
        print(f"⏱️  [Timeline] Удержание кадра ({duration_seconds}s, {total_frames} кадров)...")

        if self.current_obj:
            latex_str = self.current_obj.to_latex() if hasattr(self.current_obj, "to_latex") else str(self.current_obj)
            frame = self._render_latex_frame(latex_str)
            for _ in range(total_frames):
                if self.video_writer:
                    self.video_writer.write(frame)

    def shift_delta(self, variable, destination: float, duration_seconds: float = 1.0):
        total_frames = int(self.fps * duration_seconds)
        var_name = getattr(variable, "name", "x")
        print(f"🔄 [Timeline] Анимация shift_delta '{var_name}' -> {destination} ({total_frames} кадров MP4)...")

        start_val = variable.value
        step = (destination - start_val) / max(total_frames, 1)

        for i in range(total_frames):
            variable.value = start_val + step * (i + 1)
            if self.current_obj:
                latex_str = self.current_obj.to_latex() if hasattr(self.current_obj, "to_latex") else str(self.current_obj)
            else:
                latex_str = f"{var_name} = {variable.get_formatted_value()}"

            frame = self._render_latex_frame(latex_str)
            if self.video_writer:
                self.video_writer.write(frame)

    def export_video(self):
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None

        print(f"🎬 [Kine MP4 Engine] Сборка видео завершена: {self.output_path}")

        if sys.platform == "win32" and os.path.exists(self.output_path):
            print(f"🚀 Автоматический запуск MP4: {self.output_path}")
            os.startfile(self.output_path)


timeline = Timeline()