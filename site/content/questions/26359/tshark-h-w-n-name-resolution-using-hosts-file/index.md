+++
type = "question"
title = "tshark -H -W n name resolution using hosts file"
description = '''I&#x27;m trying to resolve ip addresses using a hosts file and it works well with the wireshark GUI (1.8.7) when the hosts file is in my Personal Configuration folder. Now I came across the tshark -H &amp;lt;hosts file&amp;gt; which seemed quite interesting  -H &amp;lt;hosts file&amp;gt; read a list of entries from a ho...'''
date = "2013-10-24T05:29:00Z"
lastmod = "2013-10-24T06:49:00Z"
weight = 26359
keywords = [ "-w", "tshark", "-h", "n" ]
aliases = [ "/questions/26359" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -H -W n name resolution using hosts file](/questions/26359/tshark-h-w-n-name-resolution-using-hosts-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26359-score" class="post-score" title="current number of votes">0</div><span id="post-26359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to resolve ip addresses using a hosts file and it works well with the wireshark GUI (1.8.7) when the hosts file is in my Personal Configuration folder. Now I came across the <code>tshark -H &lt;hosts file&gt;</code> which seemed quite interesting</p><pre><code>  -H &lt;hosts file&gt;       read a list of entries from a hosts file, which will
            then be written to a capture file. (Implies -W n)</code></pre><p>So I tried the following command that <code>will save host name resolution records along with captured packets.</code> as per <a href="http://www.wireshark.org/docs/man-pages/tshark.html">http://www.wireshark.org/docs/man-pages/tshark.html</a></p><p><code>tshark -r swg186.pcapng -H hosts -w swg186.dns.pcapng -F pcapng -W n</code></p><p>Well, obviously it didn't :-( - or I'm not seeing it...</p><p>Am i missing something here?</p><hr /><p>Yes, resolution works on other machine without external host file. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_103.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link--w" rel="tag" title="see questions tagged &#39;-w&#39;">-w</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link--h" rel="tag" title="see questions tagged &#39;-h&#39;">-h</span> <span class="post-tag tag-link-n" rel="tag" title="see questions tagged &#39;n&#39;">n</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '13, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Oct '13, 06:45</strong> </span></p></div></div><div id="comments-container-26359" class="comments-container"><span id="26363"></span><div id="comment-26363" class="comment"><div id="post-26363-score" class="comment-score"></div><div class="comment-text"><p>Looks like it actually did what it was supposed to do... Every address is now resolved - even without a matching hosts file in the wireshark GUI.<br />
Will send it to another machine and check</p></div><div id="comment-26363-info" class="comment-info"><span class="comment-age">(24 Oct '13, 06:08)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-26359" class="comment-tools"></div><div class="clear"></div><div id="comment-26359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26365"></span>

<div id="answer-container-26365" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26365-score" class="post-score" title="current number of votes">0</div><span id="post-26365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Answering my own - stupid? - question ... The name resolution is done without any external resources (hosts file or DNS) once the command</p><pre><code>tshark -r swg186.pcapng -H hosts -w swg186.dns.pcapng -F pcapng -W n</code></pre><p>is issued. This information is stored (somewhere) in the pcapng file.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-26365" class="comments-container"></div><div id="comment-tools-26365" class="comment-tools"></div><div class="clear"></div><div id="comment-26365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

