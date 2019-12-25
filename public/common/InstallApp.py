import os


def installApp():
    os.system('ios-deploy --id 00008030-00161C5C2280802E --bundle /Users/ios/Desktop/ios/ios-airtest/app/XZTenant.app')


def unInstallApp():
    os.system('ios-deploy --id 00008030-00161C5C2280802E --uninstall_only '
              '--bundle_id xiaozhu.com.XZTenant')

unInstallApp()