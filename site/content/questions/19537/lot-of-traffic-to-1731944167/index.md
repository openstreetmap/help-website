+++
type = "question"
title = "Lot of traffic to 173.194.41.67"
description = '''I am running wireshark on my laptop and am seeing a lot of traffic going to and from the above IP address. It all follows roughly the same format cadsi-lm &amp;gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0 atex-elmd &amp;gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0 f-ser &amp;gt; https [ACK] ...'''
date = "2013-03-15T06:12:00Z"
lastmod = "2013-03-19T14:34:00Z"
weight = 19537
keywords = [ "-", "https" ]
aliases = [ "/questions/19537" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lot of traffic to 173.194.41.67](/questions/19537/lot-of-traffic-to-1731944167)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19537-score" class="post-score" title="current number of votes">0</div><span id="post-19537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running wireshark on my laptop and am seeing a lot of traffic going to and from the above IP address.</p><p>It all follows roughly the same format</p><pre><code>cadsi-lm &gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0
atex-elmd &gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0
f-ser &gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0
cad-key &gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0
iclpv-pm&gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0
cichlid &gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0
molly &gt; https [ACK] SEQ = 2063 ACK= 4052 WIN=65740 LEN = 0</code></pre><p>so on and so forth - there seems to be slight variations in the IP address</p><p>Havent a clue what it is - can anybody give me any pointers please</p><p>Cheers Glenn</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link--" rel="tag" title="see questions tagged &#39;-&#39;">-</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '13, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/d92adf64d9e798e90499332a346b51a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="job3210&#39;s gravatar image" /><p><span>job3210</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="job3210 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Mar '13, 06:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-19537" class="comments-container"></div><div id="comment-tools-19537" class="comment-tools"></div><div class="clear"></div><div id="comment-19537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19538"></span>

<div id="answer-container-19538" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19538-score" class="post-score" title="current number of votes">1</div><span id="post-19538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure what it is exactly, but...</p><pre><code>$ nslookup 173.194.41.67
Server:     192.168.1.20
Address:    192.168.1.20#53

Non-authoritative answer:
67.41.194.173.in-addr.arpa  name = lhr08s01-in-f3.1e100.net.</code></pre><p>And 1e100.net points to google, see <a href="http://support.google.com/bin/answer.py?hl=en&amp;answer=174717">http://support.google.com/bin/answer.py?hl=en&amp;answer=174717</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19538" class="comments-container"><span id="19539"></span><div id="comment-19539" class="comment"><div id="post-19539-score" class="comment-score"></div><div class="comment-text"><p>Cheers for having a look Just seems odd - that there was nothing open on the laptop at the time - and I closed as many apps down as I could - but thanks again</p></div><div id="comment-19539-info" class="comment-info"><span class="comment-age">(15 Mar '13, 06:32)</span> <span class="comment-user userinfo">job3210</span></div></div><span id="19540"></span><div id="comment-19540" class="comment"><div id="post-19540-score" class="comment-score"></div><div class="comment-text"><p>If it is a windows laptop, you can use <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">netmon</a> to look at the traffic and see which process is responsible for it...</p><p>(there is work being done to make that possible with Wireshark too, but it's not finished yet)</p></div><div id="comment-19540-info" class="comment-info"><span class="comment-age">(15 Mar '13, 06:44)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-19538" class="comment-tools"></div><div class="clear"></div><div id="comment-19538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19663"></span>

<div id="answer-container-19663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19663-score" class="post-score" title="current number of votes">0</div><span id="post-19663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>that there was nothing open on the laptop at the time - and I closed as many apps down as I could - but thanks again</p></blockquote><p>If you connect to that IP address with HTTPS, it will present a certificate that is valid for a broad range of domains, including google analytics, google apis, youtube, etc.</p><pre><code>  *.google.com , *.android.com , *.appengine.google.com , *.cloud.google.com , *.google-analytics.com , *.google.ca , *.google.cl , *.google.co.in , *.google.co.jp , *.google.co.uk , *.google.com.ar , *.google.com.au , *.google.com.br , *.google.com.co , *.google.com.mx , *.google.com.tr , *.google.com.vn , *.google.de , *.google.es , *.google.fr , *.google.hu , *.google.it , *.google.nl , *.google.pl , *.google.pt , *.googleapis.cn , *.googlecommerce.com , *.gstatic.com , *.urchin.com , *.url.google.com , *.youtube-nocookie.com , *.youtube.com , *.ytimg.com , android.com , g.co , goo.gl , google-analytics.com , google.com , googlecommerce.com , urchin.com , youtu.be , youtube.com  </code></pre><p>I bet, there is some software (maybe a service) on your system that uses one of those sites to either use a google API or to update data sets (google analytics, youtube, etc.).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '13, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19663" class="comments-container"></div><div id="comment-tools-19663" class="comment-tools"></div><div class="clear"></div><div id="comment-19663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

