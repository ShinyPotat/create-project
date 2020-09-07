function global:create($ProyectName)
{
    Set-Location $env:PROJECTSFOLDER
    mkdir $ProyectName
    Set-Location $env:PROJECTSFOLDER\$ProyectName
    git init
    create.py $ProyectName
    git remote add origin https://github.com/ShinyPotat/$ProyectName.git
    Write-Output $null >> README.md
    git add .
    git commit -m "initial commit"
    git push -u origin master
    code .
}