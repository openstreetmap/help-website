+++
type = "question"
title = "Receive only broadcast in mirrored port"
description = '''I&#x27;m connected on a switch where my port receive traffic of another port monitored. I have tried Wireshark on my Window7 laptop and also with a Fedora LiveCD in another laptop. The only packets I see is broadcast multicast packets. Also with other laptop and older version of Wireshark I get only broa...'''
date = "2013-09-05T04:34:00Z"
lastmod = "2013-09-09T01:58:00Z"
weight = 24374
keywords = [ "broadcast", "capture", "captureerror" ]
aliases = [ "/questions/24374" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Receive only broadcast in mirrored port](/questions/24374/receive-only-broadcast-in-mirrored-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24374-score" class="post-score" title="current number of votes">0</div><span id="post-24374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm connected on a switch where my port receive traffic of another port monitored. I have tried Wireshark on my Window7 laptop and also with a Fedora LiveCD in another laptop. The only packets I see is broadcast multicast packets.</p><p>Also with other laptop and older version of Wireshark I get only broadcast and multicast packets or packets directed to the local pc. Nothing from the port monitored!</p><p>Also tried with an old hub..</p><p>What can I check: i'm using promiscuos mode and wired interfaces..</p><p>ADDITIONAL INFO: One partner is a gigabit eth of laptop, the other is a linux server in gigabit. The two cables are connected to a SIXNET Managed switch 10/100 and the laptop connected to monitoring port is a gigabit eth laptop.</p><p>Trying with tcpdump doesn't change anything.</p><p>The two hubs tried are made by a "non-commercial" vendor but are 10/100.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-captureerror" rel="tag" title="see questions tagged &#39;captureerror&#39;">captureerror</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '13, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/aa7629af47c063e43f6ed0b586c7bffb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MauroDx&#39;s gravatar image" /><p><span>MauroDx</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MauroDx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Sep '13, 23:38</strong> </span></p></div></div><div id="comments-container-24374" class="comments-container"><span id="24388"></span><div id="comment-24388" class="comment"><div id="post-24388-score" class="comment-score"></div><div class="comment-text"><p>what's the speed of the monitored port? what's the make and model of the hub? you can check if port span was set up to mirror both RX &amp; TX</p></div><div id="comment-24388-info" class="comment-info"><span class="comment-age">(05 Sep '13, 11:02)</span> <span class="comment-user userinfo">net_tech</span></div></div><span id="24401"></span><div id="comment-24401" class="comment"><div id="post-24401-score" class="comment-score"></div><div class="comment-text"><p>Try also using <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a> on your Windows machine and tcpdump on the Fedora LiveCD machine, but I suspect they probably won't work any better; it's probably an issue with the configuration of the switch, as net_tech suggested.</p></div><div id="comment-24401-info" class="comment-info"><span class="comment-age">(05 Sep '13, 17:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24467"></span><div id="comment-24467" class="comment"><div id="post-24467-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The two cables are connected to a SIXNET Managed switch 1</p></blockquote><p>can you please post the screenshot of the port mirroring configuration? Maybe there is a problem with that!?!</p><blockquote><p>Also tried with an old hub..</p></blockquote><p>well, that makes a config problem less likely.</p></div><div id="comment-24467-info" class="comment-info"><span class="comment-age">(09 Sep '13, 01:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24374" class="comment-tools"></div><div class="clear"></div><div id="comment-24374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

