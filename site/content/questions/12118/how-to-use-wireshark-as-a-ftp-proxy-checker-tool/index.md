+++
type = "question"
title = "How to use Wireshark as a FTP proxy checker tool"
description = '''How to use Wireshark as a FTP proxy checker tool when using various FTP clients uploading to a proxy server with a proxifying program for the FTP client. How can Wireshark confirm files are being transmitted through the port tunneling to the proxy server? Browser proxy can be checked with www.whatis...'''
date = "2012-06-21T17:13:00Z"
lastmod = "2012-06-21T22:23:00Z"
weight = 12118
keywords = [ "ftp", "checker", "proxy" ]
aliases = [ "/questions/12118" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use Wireshark as a FTP proxy checker tool](/questions/12118/how-to-use-wireshark-as-a-ftp-proxy-checker-tool)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12118-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to use Wireshark as a FTP proxy checker tool when using various FTP clients uploading to a proxy server with a proxifying program for the FTP client. How can Wireshark confirm files are being transmitted through the port tunneling to the proxy server? Browser proxy can be checked with <a href="http://www.whatismyipadress.com">www.whatismyipadress.com</a>. Where are the instructions on how can FTP uploading by proxy be checked with Wireshark?</p></div><div id="question-tags" class="tags-container tags">ftp checker proxy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '12, 17:13</strong></p><img src="https://secure.gravatar.com/avatar/57559a751370888fa3b4c144bf15d9a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wibon2&#39;s gravatar image" /><p>wibon2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wibon2 has no accepted answers">0%</span></p></div></div><div id="comments-container-12118" class="comments-container"></div><div id="comment-tools-12118" class="comment-tools"></div><div class="clear"></div><div id="comment-12118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12119"></span>

<div id="answer-container-12119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12119-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not a proxy checker, it is a network packet recording and analysis tool. So yes, you can try to diagnose and determine where packets come from and go to, but unless you're able to record the packets on their way via a proxy you're out of luck.</p><p>So you could capture in front of the FTP server and determine from what IPs the uploads come in, and then compare the IPs to known client IPs. If they're different, it's probably a proxy. If you do not know the client IPs you'll have to guess, but it is probably not going to work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '12, 17:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12119" class="comments-container"></div><div id="comment-tools-12119" class="comment-tools"></div><div class="clear"></div><div id="comment-12119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12125"></span>

<div id="answer-container-12125" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12125-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are basically three types of proxies for ftp.</p><ul><li><strong>http (web) proxy</strong><br />
You can configure a http (web) proxy for some ftp clients (Filezilla). In that case, the client will use http to communicate with the proxy. Within that protocol it will request the ftp data with <a href="ftp://host/file.">ftp://host/file.</a> So, to detect the use of a proxy in this case, just look for URLs in the capture file that start with ftp://.<br />
<strong>Filter:</strong> ip.addr eq x.x.x.x and tcp contains "ftp://", where x.x.x.x is your client ip.<br />
This will also detect browsers trying to access an ftp server. You can check the 'User-Agent' header in the http request.<br />
<br />
</li><li><strong>A "regular" ftp proxy</strong><br />
In this case your ftp clients connect to a ftp proxy, by opening a connection to the proxy ip with the ftp protocol and then they open a connection the the target server with the SITE or OPEN command. There are also proxies, that accept a special syntax for the user account and the password, like this: [email protected] They will relay the ftp connection to the target host. See Filezilla docs for this feature or the KB of <a href="https://kb.bluecoat.com/index?page=content&amp;id=KB3438">Blue Coat</a> or <a href="http://www.m86security.com/kb/article.aspx?id=13497">M86 Security</a>. You can detect the use of such a proxy, by looking for SITE, OPEN commands in the ftp control connection or by searching for USER commands with an @ char in it.<br />
<strong>Filter:</strong> ip.addr eq x.x.x.x and (ftp contains "SITE" or ftp contains "OPEN").<br />
Finding the special user name syntax is a bit tricky, as you cannot use regular expressions within the display filters.<br />
<br />
</li><li><strong>a transparent ftp proxy</strong><br />
you can detect this as described by @Jasper, or by using wrong ftp commands. Sometimes transparent ftp proxies answer with non-standard error messages and reveal their existence in this way. However, you cannot use this method within wireshark. You have to do it in the ftp client.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '12, 22:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jun '12, 22:28</p></div></div><div id="comments-container-12125" class="comments-container"></div><div id="comment-tools-12125" class="comment-tools"></div><div class="clear"></div><div id="comment-12125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

