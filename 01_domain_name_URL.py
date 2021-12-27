def domain_name(url):
    # domain = url.split(".")[-2].split("/")[-1]
    # domain = url.lstrip("https://www.").split(".")[0]
    domain = url.replace("www.", "").split(".")[0].split("/")[-1]

    print(domain)
    return domain


domain_name("http://github.com/carbonfive/raygun")
domain_name("http://www.zombie-bites.com")
domain_name("https://www.cnet.com")
domain_name("https://www.cnet.co.uk")
domain_name("www.xaker.ru")
