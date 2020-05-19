import requests

cookies = {
    "AWSALB": "U9P+mqu+ul6rOopLOCPEJtLjHBoZEdZ4ZE1za9RrT94iCtU3Lq6Yxwclvp950Wmrfqgqm9CziFh4w2+5W+b5p3YE+MdVU3TabTvVPdr3eijMWNyJQmHMgZnJ1LKFqkV+Up7Ypo2iT/ZaZ5+wWDoOEB6HziSSBLlUoC0kJULSVjmEr2ZJvWPp48oozeeKwQ==",
    "AWSALBCORS": "U9P+mqu+ul6rOopLOCPEJtLjHBoZEdZ4ZE1za9RrT94iCtU3Lq6Yxwclvp950Wmrfqgqm9CziFh4w2+5W+b5p3YE+MdVU3TabTvVPdr3eijMWNyJQmHMgZnJ1LKFqkV+Up7Ypo2iT/ZaZ5+wWDoOEB6HziSSBLlUoC0kJULSVjmEr2ZJvWPp48oozeeKwQ==",
    "JSESSIONID_JX_APP": "0BDD280D9CECC5688DA64093916CDF93",
    "GSESSIONID": "0BDD280D9CECC5688DA64093916CDF93",
    "cass": "2",
    "gdId": "b4c000b7-8da4-4e3a-b7d3-d763b5853437",
    "trs": "https%3A%2F%2Fwww.google.com%2F:SEO:SEO:2020-05-15+08%3A43%3A34.913:undefined:undefined",
    "uc": "8F0D0CFA50133D96DAB3D34ABA1B873324E3F5DA1D1CA8D53F7CDB15E0E972C88D8AF602813C5C4B348C3B29B3D04FF6325FD44230E522ACB46583BD23C57828C2FBC611438D6AC5EADA5958631E5766560ECF96BB9E0E1FAD47A374747D57367132A826024F7838F5DC9EF2C2FB8E598ED15531EE8C8BE5785D2F986D552DE68F6EFE586167296FD796FE79C9B653DD8F21A9CC698B2D9E",
    "__cf_bm": "4195cf159ad28f06152c8f9974c48be9971dbfb5-1589557416-1800-AT3yTkG71snT3BU7YKBRI2C8EMOLext3Rb5ID3yS3FpTC0X3a0WAYaQEuMJzGPKTUR6KgTtAYo0YZ5Yfrp/FFo0=",
    "JSESSIONID": "A24131B2B06B3E460911D6521FB07274",
    "G_ENABLED_IDPS": "google",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.glassdoor.com",
    "DNT": "1",
    "Referer": "https://www.glassdoor.com/",
    "Connection": "keep-alive",
    "TE": "Trailers",
}

data = {
    "sc.keyword": "Correctional Officer",
    "locT": "C",
    "locId": "1132348",
    "p": "2",
    "gdToken": "zxivOtrrYFhBnyuufzmvFA:nru0WliYc7OKL-kurWxO12F0I99DC2hgXdm0Upqhrtw6s62GVOy3F2GjAEARcf5VbvLGeL2u-L4JLJMei5CHXg:mLm_JyKq3dYx1Mu03tNRduXse-FSyU563XwWEWxy23A",
}

response = requests.post(
    "https://www.glassdoor.com/Job/json/search.htm",
    headers=headers,
    cookies=cookies,
    data=data,
)


data = response.json()
jobs = data["jobListings"]

for item in jobs:
    title = item["jobTitle"]
    employer = item["employer"]["name"]
    print(title, employer)
