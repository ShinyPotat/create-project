function global:create($ProyectName)
{
    Set-Location C:\Users\JaviP\Documents\Proyectos\MisProyectos
    mkdir $ProyectName
    Set-Location C:\Users\JaviP\Documents\Proyectos\MisProyectos\$ProyectName
    git init
    python C:\Users\JaviP\Documents\Proyectos\MisProyectos\create-project\create.py $ProyectName
    git remote add origin https://github.com/ShinyPotat/$ProyectName.git
    Write-Output $null >> README.md
    git add .
    git commit -m "initial commit"
    git push -u origin master
    code .
}