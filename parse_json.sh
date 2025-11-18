#! /bin/env bash
input="$1"

filename=$(basename "$input")
filename="${filename%.*}"
dirname=$(dirname "$input")
outdir="./staging/csv"
outfile="$outdir/$filename.csv"
source processor.env
if [ ! -f "$input" ]
then
    echo "$input does not exist"
    exit 
fi

echo "Processing $input into $outfile"

manual_vault=$local_vault
echo "$local_vault"
if [ ! -d "$manual_vault" ]
then
    echo "Local vault: $manual_vault does not exist"
    exit
fi

#/samsung980pro1/manual_vault/
echo "Downloading into $manual_vault"
python patreonprocessor/parse_patreon_json.py "$input" "$outfile" --download "$manual_vault"

echo "$remote_address"
rsync -av "$manual_vault" "$remote_address"
scp $outfile "$ingest_address"
#armorclad@manatarms:/u01/vault/


