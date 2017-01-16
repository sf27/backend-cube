rm -rf ./logs
mkdir ./logs

function execute(){
  local _command=$1
  local _name=$2
  echo "execute: $_command"
  _file="./logs/$_name.log"
  eval $_command > $_file
  output_command=$?
  if [ $output_command -ne 0 ];then
    echo "!!!!!!!!                                             !!!!!!!!"
    echo "!!!!!!!!                 Have errors                 !!!!!!!!"
    echo "!!!!!!!!                                             !!!!!!!!"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    cat $_file
    rm -rf ./logs
    exit
  fi
}

# list of commands
execute "isort -c -rc -df" isort
execute "flake8" flake8
execute "python manage.py test" tests

echo "!!!!!!!!                                             !!!!!!!!"
echo "!!!!!!!!             All perfect man                 !!!!!!!!"
echo "!!!!!!!!                                             !!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
rm -rf ./logs