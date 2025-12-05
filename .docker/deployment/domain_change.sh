
docker_address="http://host.docker.internal:3030/rocrate/sparql"
local_address="http://localhost:3030/rocrate/sparql"
server_address="https://query.ro-crate.org/rocrate/sparql"

files=( "src/configs/rocrate/search_perspectives/profiles.json"
        "src/configs/portalConfig.json" )
        
        
for file in ${files[@]}; do
    sed -e "s|${docker_address}|${server_address}|g" \
        -e "s|${local_address}|${server_address}|g" ${file} > ${file}.temp
    mv ${file}.temp $file
done