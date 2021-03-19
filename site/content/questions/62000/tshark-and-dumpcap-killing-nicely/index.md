+++
type = "question"
title = "tshark and dumpcap - killing &quot;nicely&quot;"
description = '''Hi, I have a shell script which uses tshark to monitor incoming video traffic, created by an ffmpeg process launched from the same script.  I want to capture until another process ends - so ideally until there has been a gap of X seconds since the last packet was captured. I can&#x27;t find a way to spec...'''
date = "2017-06-14T02:43:00Z"
lastmod = "2017-06-14T07:12:00Z"
weight = 62000
keywords = [ "tshark", "kills", "dumpcap" ]
aliases = [ "/questions/62000" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark and dumpcap - killing "nicely"](/questions/62000/tshark-and-dumpcap-killing-nicely)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62000-score" class="post-score" title="current number of votes">0</div><span id="post-62000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a shell script which uses tshark to monitor incoming video traffic, created by an ffmpeg process launched from the same script.</p><p>I want to capture until another process ends - so ideally until there has been a gap of X seconds since the last packet was captured. I can't find a way to specify this using parameters, but have managed to almost solve it by capturing the tshark pid, then killing it when the process it is monitoring ends.</p><p>This is not a problem on the face of it, since I capture the tshark PID at process start. However, when I do this the dumpcap process is often left running forever...</p><p>Any ideas how I can kill both tshark and the dumpcap process it has created...?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-kills" rel="tag" title="see questions tagged &#39;kills&#39;">kills</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '17, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/ed56b38042032c7d46130c321dbcbd7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbrb2&#39;s gravatar image" /><p><span>dbrb2</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbrb2 has no accepted answers">0%</span></p></div></div><div id="comments-container-62000" class="comments-container"></div><div id="comment-tools-62000" class="comment-tools"></div><div class="clear"></div><div id="comment-62000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62001"></span>

<div id="answer-container-62001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62001-score" class="post-score" title="current number of votes">0</div><span id="post-62001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you need tshark decoding the incoming packets? If not - meaning you're only interested in capturing the packets, not any packet details during capture - you could just run dumpcap instead of tshark from your script and kill it instead directly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '17, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-62001" class="comments-container"><span id="62003"></span><div id="comment-62003" class="comment"><div id="post-62003-score" class="comment-score"></div><div class="comment-text"><p>Possibly - currently I run tshark to capture the traffic from a particular source (since there will be traffic from many sources on the interface) and save it to a pcap file:</p><p>$TSHARK -i $INTF -w $PCAP host $IP &gt; /dev/null 2&gt;&amp;1&amp;</p><p>At a later stage, I then decode and analyse this data: $TSHARK -r $PCAP -d udp.port==$PORT_RANGE,rtp -T fields -e rtp.seq &gt; $FILE 2&gt; /dev/null&amp;</p><p>It is the first command that occasionally hangs. Am I right in thinking that dumpcap can do the filtering - it is the decoding of protocols that tshark brings - meaning I could use:</p><p>$DUMPCAP -i $INTF -w $PCAP -f "host $IP" &gt; /dev/null 2&gt;&amp;1&amp;</p></div><div id="comment-62003-info" class="comment-info"><span class="comment-age">(14 Jun '17, 02:58)</span> <span class="comment-user userinfo">dbrb2</span></div></div><span id="62004"></span><div id="comment-62004" class="comment"><div id="post-62004-score" class="comment-score"></div><div class="comment-text"><p>dumpcap does the BPF filtering, so if you're using capture filters (like it looks you are) it can do that. I always recommend running dumpcap directly instead of Wireshark/tshark because it's much leaner and less prone to crash due to out-of-memory situations.</p></div><div id="comment-62004-info" class="comment-info"><span class="comment-age">(14 Jun '17, 03:11)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="62005"></span><div id="comment-62005" class="comment"><div id="post-62005-score" class="comment-score"></div><div class="comment-text"><p>That looks like it is going to work - so I am now using dumpcap to capture, using a capture filter to grab only those from a source IP I am interested in, and saving to a pcap file. Later, I use tshark to decode this traffic by reading in the pcap file.</p></div><div id="comment-62005-info" class="comment-info"><span class="comment-age">(14 Jun '17, 03:19)</span> <span class="comment-user userinfo">dbrb2</span></div></div></div><div id="comment-tools-62001" class="comment-tools"></div><div class="clear"></div><div id="comment-62001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62008"></span>

<div id="answer-container-62008" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62008-score" class="post-score" title="current number of votes">0</div><span id="post-62008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While Jasper's answer is the better overall solution I'll try to answer the initial question.</p><p>tshark catches both SIGINT and SIGTERM and (tries to) clean up its child process (dumpcap) after catching those signals--so <code>kill &lt;pid of tshark&gt;</code> <em>should</em> work (since kill uses SIGTERM by default).</p><p>You mention that it "often" doesn't work which is odd; I tried a few times here (with a fairly old version, no less) and it worked each time. There may be a problem lurking here but unless you're using a different signal (like SIGKILL) you were already killing tshark the "nice" way.</p><p><strong>UPDATE</strong></p><p>Actually it occurs to me that if you were using a signal other than SIGINT or SIGTERM then that could explain the behavior you were seeing: the SIGKILL would clearly kill tshark without allowing it to clean up dumpcap. Now IFF no more packets were received then dumpcap would hang around doing nothing. As soon as another packet is received, however, dumpcap will try to send a notification to tshark and should then get a SIGPIPE which would kill off dumpcap. (You mentioned that you were killing tshark after a test was completed which could mean "no more packets for a while.")</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '17, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '17, 07:24</strong> </span></p></div></div><div id="comments-container-62008" class="comments-container"><span id="62014"></span><div id="comment-62014" class="comment"><div id="post-62014-score" class="comment-score"></div><div class="comment-text"><p>I agree with Jasper and Jeff too, but if for some reason dbrb2 really wants to use <code>SIGKILL</code>, then the process group could be specified instead of the process ID and that should work. For example:</p><pre><code>[[email protected] ~]$ pidof tshark dumpcap
11873 11876
[[email protected] ~]$ kill -SIGKILL -`pidof tshark`
[[email protected] ~]$ pidof tshark dumpcap
[[email protected] ~]$</code></pre><p>As opposed to only killing tshark via <code>SIGKILL</code>:</p><pre><code>[[email protected] ~]$ pidof tshark dumpcap
11908 11911
[[email protected] ~]$ kill -SIGKILL `pidof tshark`
[[email protected] ~]$ pidof tshark dumpcap
[[email protected] ~]$ 11911</code></pre></div><div id="comment-62014-info" class="comment-info"><span class="comment-age">(14 Jun '17, 07:12)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-62008" class="comment-tools"></div><div class="clear"></div><div id="comment-62008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

