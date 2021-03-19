+++
type = "question"
title = "how to detect ddos attacks on my network"
description = '''how to detect ddos attacks on my network in purpose to reduce my internet connectivity i&#x27;m new in wireshark please answer easily as u can'''
date = "2017-04-12T07:18:00Z"
lastmod = "2017-04-12T10:55:00Z"
weight = 60763
keywords = [ "attacks", "detection", "ddos" ]
aliases = [ "/questions/60763" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to detect ddos attacks on my network](/questions/60763/how-to-detect-ddos-attacks-on-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60763-score" class="post-score" title="current number of votes">0</div><span id="post-60763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to detect ddos attacks on my network in purpose to reduce my internet connectivity i'm new in wireshark please answer easily as u can</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-attacks" rel="tag" title="see questions tagged &#39;attacks&#39;">attacks</span> <span class="post-tag tag-link-detection" rel="tag" title="see questions tagged &#39;detection&#39;">detection</span> <span class="post-tag tag-link-ddos" rel="tag" title="see questions tagged &#39;ddos&#39;">ddos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '17, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/8e22686656579707bd87dc381c08910b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="isaak&#39;s gravatar image" /><p><span>isaak</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="isaak has no accepted answers">0%</span></p></div></div><div id="comments-container-60763" class="comments-container"><span id="60765"></span><div id="comment-60765" class="comment"><div id="post-60765-score" class="comment-score"></div><div class="comment-text"><p>What makes you think you are suffering a DDOS and how are you connecting to the Internet, cable modem, DSL modem, 4G wireless or something else?</p></div><div id="comment-60765-info" class="comment-info"><span class="comment-age">(12 Apr '17, 08:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60769"></span><div id="comment-60769" class="comment"><div id="post-60769-score" class="comment-score"></div><div class="comment-text"><p>wireless network</p></div><div id="comment-60769-info" class="comment-info"><span class="comment-age">(12 Apr '17, 09:43)</span> <span class="comment-user userinfo">isaak</span></div></div></div><div id="comment-tools-60763" class="comment-tools"></div><div class="clear"></div><div id="comment-60763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60774"></span>

<div id="answer-container-60774" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60774-score" class="post-score" title="current number of votes">1</div><span id="post-60774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Isaak</p><p>DDoS attacks come in a large variety. Here are a few of them:</p><p><strong>Reflection attacks</strong></p><p>The attacks abuse a feature of a UDP based protocol where a small request triggers a large response. DNS and NTP have certain features that allow this type of abuse.</p><p><strong>Spotting reflection attacks</strong></p><ul><li>Locate DNS/NTP responses for which your system never send a request. <strong><code>udp.srcport == 53 or udp.srcport == 123</code></strong> would be the proper display filters</li><li>The response can easily exceed the maximum size of an Ethernet frame. Look out for IP fragmentation. A number of display filters will help. <strong><code>ip.frag_offset &gt; 0</code></strong> is one of them.</li><li>Please note, that the IP continuation packets will not hold the UDP port numbers. Wireshark supports IP fragment reassembly, so that the total message will be dissected.</li></ul><p><strong>TCP SYN floods</strong></p><p>These attacks try to fill the state table in a firewall or try to overwhelm a server's buffer. A number of techniques exists to defend against this type of attack. TCP SYN cookies are one of them.</p><p><strong>Detecting SYN floods</strong></p><ul><li>Look out for an immense number of TCP connection requests. The proper display filter is <strong><code>tcp.flags.syn == 1 and tcp.flags.ack == 0</code></strong></li><li>The server, that is under attack, will respond with a smaller number of SYN/ACKs. These can be spotted with the display filter <strong><code>tcp.flags.syn == 1 and tcp.flags.ack == 1</code></strong></li><li>Try to compare the number of SYNs with the number of SYN/ACKs. As long as the numbers are identical your firewall or server is holding up.</li><li>Very often, the source addresses are spoofed. A good indicator of a spoofed source address is a packet with the RST bit set in response to the SYN/ACK from your server. The normal response would be a packet with just the ACK flag being set.</li></ul><p><strong>Attacks against layer 7 on your web servers.</strong></p><p>Most web servers have a search function, user registration dialog or similar function, that triggers a lengthy response in the backend. An attacker can identify suitable targets by examining the HTTP response time. Some websites can be brought down by a surprisingly small number of parallel HTTP requests that trigger searches, process log on data or the check out process in a web store.</p><p><strong>Spotting layer 7 attacks</strong></p><ul><li>Your best bet is the web server's log file, especially if you are using HTTPS. (You hopefully use SSL, don't you?) Try to spot frequently called URIs in the log file.</li><li>Look out for user agents that indicate automated access. Among the candidates are wget or curl.</li><li>If you have access to unencrypted traffic, try create a separate profile and add columns for the user agent <strong><code>http.user_agent</code></strong> and for the URI <strong><code>http.request.uri</code></strong></li><li>Check if HTTP requests come with a referrer, where it is reasonable to expect them. Access to the check-out function in a web store without a referrer would be odd. Add <strong><code>http.referer</code></strong> as another column.</li></ul><p><strong>Geographic distribution of IP addresses</strong></p><p>Most web sites have a distinct pattern, when users from a certain geographic region visit the site. A web site for a school or college would mostly draw traffic from local or regional IP addresses. Also, expect a few search engines and crawlers. A sudden surge in requests from rather remote locations would be an indicator of an attack.</p><p>This wireshark web site is visited by an international community. I have never seen the log files for this server. Still, I would expect over a 24 hour time window visitors from all over the world. Just looking at the log files for 10 am European time I would expect mostly European visitors, plus a few night owls from the Asian-Pacific region and a few early risers from the Americas.</p><p>A good baseline helps in spotting the attacks. Wireshark can pinpoint the location of an IP address. Check out the <a href="https://wiki.wireshark.org/HowToUseGeoIP">Wireshark Wiki</a> for details</p><p><strong>DDoS by Popularity</strong></p><p>While aforementioned school web server is mostly idle, it can attract a huge surge of legitimate traffic. Expect a serious flood of traffic, if major news networks report about the school and place a link on their site. Something similar could happen, if a social media user with millions of friends or followers mentions your web site.</p><p><strong>General hints</strong></p><p>Some tools used for network flooding define constants in some fields in the IP or TCP header, where a certain amount of randomness can be expected. Examples are the IP ID, the DNS transaction ID, a TCP source port number or sequence number. An excessive value of packets with a constant IP ID is an indicator for a very strange IP stack or for "hand crafted" packets.</p><p>Good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-60774" class="comments-container"></div><div id="comment-tools-60774" class="comment-tools"></div><div class="clear"></div><div id="comment-60774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

