from django.shortcuts import render
from django.http import HttpResponse

def viewserver(request):
    query = request.GET.get('s')
    if(query == '1'):
        context= {
            'web': '/ref?s=akatsuki.pw',
            'img': 'https://marc.enjuu.click/download/1930773.png',
            'servername': 'Akatsuki',
            'smalldes': 'STD & RX PP',
            'longdes': 'Akatsuki is Features Relax and STD PP',
            'players': '9111',
            'rlylongdes': 'This is the Server that runs this Server List. Our private osu! Server. It supports nearly all Gamemodes so STD, AP, RX but nerfed',
        }
        return render(request, 'home/view.html', context)
    elif(query == '2'):
        context= {
            'web': '/ref?s=enjuu.click',
            'img': 'https://enjuu.click/static/logos/logo-blue.png',
            'servername': 'Enjuu',
            'smalldes': 'STD, AP, RX PP',
            'longdes': 'Enjuu is a osu! Private Server that exist since January. Featuring RX and many more Features. ',
            'players': '504',
            'rlylongdes': 'The Akatsuki servers are two completely separate servers; one dedicated to regular osu PP, and features that youd expect from a private server; and the other featuring PP for relax plays, and a completely unique PP algorithm to fit the nature of the server.',
        }
        return render(request, 'home/view.html', context)
    elif(query == '3'):
        context= {
            'web': '/ref?s=ripple.moe',
            'img': 'https://marc.enjuu.click/download/1482369.png',
            'servername': 'Ripple',
            'smalldes': 'STD PP',
            'longdes': 'Ripple is the Private Server with the most Users. ',
            'players': '62381 ',
        }
        return render(request, 'home/nodes.html', context)
    elif(query == '4'):
        context= {
            'web': '/ref?s=osu.gatari.pw/?e',
            'img': 'https://marc.enjuu.click/download/9381005.png',
            'servername': 'Gatari',
            'smalldes': 'STD PP',
            'longdes': 'Gatari is a Russian osu Server. With a nice Clan System ',
            'players': '6778 ',
        }
        return render(request, 'home/nodes.html', context)
    elif(query == '5'):
        context= {
            'web': '/ref?s=vipsu.ml',
            'img': 'https://marc.enjuu.click/download/2325559.png',
            'servername': 'Vipsu',
            'smalldes': 'STD own weightend PP',
            'longdes': 'Vipsu is a small and new osu! Private Server ',
            'players': '19 ',
        }
        return render(request, 'home/nodes.html', context)
    elif(query == '6'):
        context= {
            'web': '/ref?s=skycircles.ru',
            'img': 'https://marc.enjuu.click/download/3832546.png',
            'servername': 'SkyCircles',
            'smalldes': 'STD PP',
            'longdes': 'SkyCircles is a new Russian osu Server ',
            'players': '91',
            'rlylongdes': 'SkyCircles is a Russian Osu! server started on February 6th, 2018. It has an active team of developers, currently working on the new frontend, backend an a new anticheat.',
        }
        return render(request, 'home/view.html', context)
    elif(query == '7'):
        context= {
            'web': '/ref?s=gigamons.de',
            'img': 'https://marc.enjuu.click/download/6312014.png',
            'servername': 'Gigamons',
            'smalldes': 'RX&TD PP',
            'longdes': 'Seperate RX Scoreboard and leaderboard. Seperate TD Scoreboard and leaderboard. Trollerino. All default bancho stuff, such as beatmap submittion. A few comming soon. (written by owner) ',
            'players': 'NONE',
        }
        return render(request, 'home/nodes.html', context)
    elif(query == '8'):
            context= {
                'web': '/ref?s=osu.xii.nz',
                'img': 'https://marc.enjuu.click/download/4484948.png',
                'servername': 'XII',
                'smalldes': 'STD PP',
                'longdes': 'XII is a small and new osu Server ',
                'players': '20',
            }
            return render(request, 'home/nodes.html', context)
    else:
        return render(request, 'home/nf.html')




def ref(request):
    query = request.GET.get('s')
    context= {
        'server': query,
    }
    return render(request, 'home/redirect.html', context)

def addserver(request):
        return render(request, 'home/addserver.html')
def add(request):
        return render(request, 'home/add.html')
def server(request):
        return render(request, 'home/servers.html')
def index(request):
        return render(request, 'home/home.html')
def nf(request):
        return render(request, 'home/nf.html')
