+++
type = "question"
title = "Miscommunication Acqknowledge software and Vizard Lite"
description = '''Hi all, I&#x27;m a PhD student in neuroscience, looking into the effects of stress on risk-taking. To this end we measure physiological signals such as heart rate and blood pressure. This measurement data is gathered by a software package called Acqknowledge, which sends it over a LAN to another pc, on w...'''
date = "2014-01-10T03:14:00Z"
lastmod = "2014-01-10T03:59:00Z"
weight = 28765
keywords = [ "rst", "sniffing" ]
aliases = [ "/questions/28765" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Miscommunication Acqknowledge software and Vizard Lite](/questions/28765/miscommunication-acqknowledge-software-and-vizard-lite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28765-score" class="post-score" title="current number of votes">0</div><span id="post-28765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm a PhD student in neuroscience, looking into the effects of stress on risk-taking. To this end we measure physiological signals such as heart rate and blood pressure. This measurement data is gathered by a software package called Acqknowledge, which sends it over a LAN to another pc, on which a Python script runs. And this is where the trouble starts: at some point, sometimes after a minute, sometimes after 30 minutes, the connection is lost between Acqknowledge and the python script.</p><p>I've used wireshark to see what happens, see for screenshots of two separate instances where it went wrong <a href="http://imgur.com/a/qRhXj">here</a> (Acqknowledge runs on 192.168.0.2 and the Python script on 192.168.0.1)</p><p>Could someone perhaps explain a little bit what happens here? I have been reading up on the TCP protocol and my layman's view of what's going on is that at some point the script sends a FIN to Acqknowledge to terminate the connection, but receives no ACK on this request and therefore sends a RST, effectively ending the connection. Is this somewhat correct or completely wrong? And has anybody perhaps noticed such a pattern before and/or has any ideas on how to approach this issue?</p><p>Any help is appreciated, cheers,</p><p>Benny</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '14, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/d6b06aa5b5af392ffcb873b3988cce26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhvijgh&#39;s gravatar image" /><p><span>bhvijgh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhvijgh has no accepted answers">0%</span></p></div></div><div id="comments-container-28765" class="comments-container"></div><div id="comment-tools-28765" class="comment-tools"></div><div class="clear"></div><div id="comment-28765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28766"></span>

<div id="answer-container-28766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28766-score" class="post-score" title="current number of votes">0</div><span id="post-28766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like the 192.168.0.1 finishes the conncection (as you already found out) in a graceful way using the FIN flag, but then gets "angry" and sends a Reset in the next packet to the other system. Looks to me like the pyhton script isn't having a patient day, maybe caused by the fact - as an reaction to the FIN - the Acqknowledge server sends <strong>more</strong> data. Maybe the script doesn't know how to handle data after FIN and simply quits. If there are any logs on that pyhton system you should check for hints that the script terminated in an error state.</p><p>BTW, screenshots are better than nothing, but if you can try to upload a (non sensitive) capture file at <a href="http://www.cloudshark.org">Cloudshark</a> and post the link. It is much easier to look at packets in an analyzer than on a screen that doesn't show everything.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '14, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28766" class="comments-container"></div><div id="comment-tools-28766" class="comment-tools"></div><div class="clear"></div><div id="comment-28766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

