# src/kine/cli.py

import argparse
import os
import sys
import time
from kine.animation.timeline import timeline


def main():
  # Гарантируем, что текущая папка и папка src есть в путях импорта Python
  current_dir = os.getcwd()
  src_dir = os.path.join(current_dir, "src")

  if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
  if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

  parser = argparse.ArgumentParser(description="Kine — Engine CLI", prog="kine")

  parser.add_argument("script", type=str, help="Путь к Python-файлу")
  parser.add_argument("scene", type=str, help="Имя сцены/класса для рендера")

  parser.add_argument(
      "-l",
      "--low-quality",
      action="store_true",
      help="Низкое качество (480p, 30 fps)",
  )
  parser.add_argument(
      "-m",
      "--medium-quality",
      action="store_true",
      help="Среднее качество (720p, 30 fps)",
  )
  parser.add_argument(
      "-hqa",
      "--high-quality",
      action="store_true",
      help="Высокое качество (1080p, 60 fps)",
  )
  parser.add_argument(
      "-k",
      "--4k",
      dest="four_k",
      action="store_true",
      help="Качество 4K (2160p, 60 fps)",
  )
  parser.add_argument(
      "-o",
      "--output",
      type=str,
      default="output.mp4",
      help="Выходной файл (по умолчанию: output.mp4)",
  )

  args = parser.parse_args()

  # 1. Сначала определяем разрешение и FPS
  resolution_str, fps = "1080p", 60
  res_tuple = (1920, 1080)

  if args.low_quality:
    resolution_str, fps = "480p", 30
    res_tuple = (854, 480)
  elif args.medium_quality:
    resolution_str, fps = "720p", 30
    res_tuple = (1280, 720)
  elif args.four_k:
    resolution_str, fps = "2160p (4K)", 60
    res_tuple = (3840, 2160)

  if not os.path.exists(args.script):
    print(f"❌ Ошибка: файл '{args.script}' не найден!")
    sys.exit(1)

  # 2. Настраиваем таймлайн ПОСЛЕ объявления fps и res_tuple
  timeline.setup(fps=fps, resolution=res_tuple, output_path=args.output)

  print("==================================================")
  print("🎬 [Kine Engine] Запуск сцены")
  print("==================================================")
  print(f"📄 Файл:         {args.script}")
  print(f"🎭 Сцена:        {args.scene}")
  print(f"⚙️  Качество:     {resolution_str} @ {fps} FPS")
  print(f"📁 Выход:        {args.output}")
  print("--------------------------------------------------")

  start_time = time.time()

  try:
    with open(args.script, "r", encoding="utf-8") as f:
      script_code = f.read()

    global_vars = {
        "__name__": "__main__",
        "__file__": os.path.abspath(args.script),
    }
    exec(script_code, global_vars)

    if args.scene in global_vars:
      scene_obj = global_vars[args.scene]
      if callable(scene_obj):
        scene_obj()
    else:
      print(f"⚠️ Предупреждение: сцена '{args.scene}' не найдена в файле.")

    # 3. Экспортируем видео после выполнения сцены
    timeline.export_video()

  except Exception as e:
    print(f"\n💥 Ошибка при выполнении:\n{e}")
    sys.exit(1)

  elapsed = time.time() - start_time
  print("--------------------------------------------------")
  print(f"✅ Рендер сцены '{args.scene}' завершен за {elapsed:.2f} сек!")


if __name__ == "__main__":
  main()