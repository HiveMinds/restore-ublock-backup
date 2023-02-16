# Restores a uBlock Origin backup into Firefox

Horrible boiler plate to restore an opinionated uBlock Origin backup into the uBlock origin extension for Firefox.

## Run
```
git clone git@github.com:HiveMinds/restore-ublock-backup.git
cd restore-ublock-backup
conda env create --file environment.yml
conda activate restore-ublock-backup
python -m src.restore_ublock_backup
```

## Warning
Deletes `snap` installation of Firefox and replaces it with an `apt` installation. You will loose your:
 - Browser history
 - Bookmarks
 - All other firefox settings.
