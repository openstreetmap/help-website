+++
type = "question"
title = "Wireshark capture &quot;Live packet&quot; from Ethernet card?"
description = '''From the info, Wireshark capture &quot;Live packet&quot; from ethernet.  Can i know where these &quot;live packet&quot; is capture?   Network Cable -&amp;gt; Ethernet card -&amp;gt; Wireshark   Network Cable -&amp;gt; Ethernet card -&amp;gt; OS -&amp;gt; TCP Stack -&amp;gt; Wireshark  I am not familiar with network. Thanks in advance !!!!'''
date = "2010-09-29T20:02:00Z"
lastmod = "2010-10-06T14:29:00Z"
weight = 370
keywords = [ "datacapture" ]
aliases = [ "/questions/370" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture "Live packet" from Ethernet card?](/questions/370/wireshark-capture-live-packet-from-ethernet-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-370-score" class="post-score" title="current number of votes">0</div><span id="post-370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From the info, Wireshark capture "Live packet" from ethernet.</p><p>Can i know where these "live packet" is capture?</p><ol><li>Network Cable -&gt; Ethernet card -&gt; Wireshark<br />
</li><li>Network Cable -&gt; Ethernet card -&gt; OS -&gt; TCP Stack -&gt; Wireshark</li></ol><p>I am not familiar with network. Thanks in advance !!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-datacapture" rel="tag" title="see questions tagged &#39;datacapture&#39;">datacapture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '10, 20:02</strong></p><img src="https://secure.gravatar.com/avatar/90eb194cf11d6309ff112d840912d03d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stan&#39;s gravatar image" /><p><span>stan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stan has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-370" class="comments-container"></div><div id="comment-tools-370" class="comment-tools"></div><div class="clear"></div><div id="comment-370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="372"></span>

<div id="answer-container-372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-372-score" class="post-score" title="current number of votes">1</div><span id="post-372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think "Live packet capture" in this case means that the network data is captured live from the network, as opposed to opening an existing, prerecorded (dead? :-)) trace file. That statement is probably there to tell you that Wireshark is not just an offline packet analysis tool, but that it can capture, too. Well, dumpcap does all the capturing work, but Wireshark is the "commanding officer" :-)</p><p>I can't describe the flow of capture downto the finest details, but I'd say it's like this: Network Cable -&gt; Ethernet Card -&gt; OS -&gt; libPCAP/WinPCAP -&gt; dumpcap.exe -&gt; tempfile -&gt; Wireshark</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '10, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-372" class="comments-container"><span id="445"></span><div id="comment-445" class="comment"><div id="post-445-score" class="comment-score"></div><div class="comment-text"><p>That's pretty much it (although there's no ".exe" on UN*X, it's just "dumpcap"). What's in the "OS" part differs from OS to OS; it starts with the driver for the Ethernet adapter, and then goes to whatever mechanism the OS provides for libpcap to use on UNIX, or goes to NDIS and then the WinPcap kernel driver on Windows.</p></div><div id="comment-445-info" class="comment-info"><span class="comment-age">(06 Oct '10, 14:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-372" class="comment-tools"></div><div class="clear"></div><div id="comment-372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

