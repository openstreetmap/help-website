+++
type = "question"
title = "Disbale &quot;cut short in the middle of a packet&quot; popup"
description = '''Is there any way to disable this &quot;cut short in the middle of a packet&quot; notification? I don&#x27;t care if it&#x27;s been cut short. This popup keeps me from being able to merge files so it&#x27;s driving me insane. '''
date = "2016-09-21T13:15:00Z"
lastmod = "2016-09-21T13:46:00Z"
weight = 55725
keywords = [ "merge", "disable", "warning", "popup" ]
aliases = [ "/questions/55725" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Disbale "cut short in the middle of a packet" popup](/questions/55725/disbale-cut-short-in-the-middle-of-a-packet-popup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55725-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to disable this "cut short in the middle of a packet" notification? I don't care if it's been cut short. This popup keeps me from being able to merge files so it's driving me insane.</p></div><div id="question-tags" class="tags-container tags">merge disable warning popup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '16, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/7369b1160530f8f7c8e2d095869bf0ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awall&#39;s gravatar image" /><p>awall<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awall has no accepted answers">0%</span></p></div></div><div id="comments-container-55725" class="comments-container"><span id="55729"></span><div id="comment-55729" class="comment"><div id="post-55729-score" class="comment-score"></div><div class="comment-text"><p>To my knowledge it can only be disabled by feeding Wireshark with properly closed files. What forces you to copy files before they have been closed and thus lose the last captured packets? Maybe use of ring buffers for capturing could solve it?</p></div><div id="comment-55729-info" class="comment-info"><span class="comment-age">(21 Sep '16, 13:48)</span> sindy</div></div></div><div id="comment-tools-55725" class="comment-tools"></div><div class="clear"></div><div id="comment-55725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55728"></span>

<div id="answer-container-55728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55728-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there any way to disable this "cut short in the middle of a packet" notification?</p></blockquote><p>No. It's reporting that the file appears to have been damaged; either 1) the file really <em>was</em> damaged, in which case you lost data from that file, or 2) there's a bug in Wireshark and it's mistakenly reporting that the file was damaged, in which case you will lose data in the merge process.</p><p>If 1) is the case, run the file through editcap, or read it into Wireshark and then write it out; that will discard the damaged parts. Then do the merge using the resulting files.</p><p>If 2) is the case, file a bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '16, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55728" class="comments-container"><span id="55732"></span><div id="comment-55732" class="comment"><div id="post-55732-score" class="comment-score"></div><div class="comment-text"><p>With the IDS I am using, I only capture a certain number of bytes per alert (due to storage space), so almost every packet is cut short, but because of this warning box the inherent merge feature will not work. I don't get why there is no option to disable warnings.</p></div><div id="comment-55732-info" class="comment-info"><span class="comment-age">(21 Sep '16, 14:40)</span> awall</div></div><span id="55733"></span><div id="comment-55733" class="comment"><div id="post-55733-score" class="comment-score"></div><div class="comment-text"><blockquote><p>With the IDS I am using, I only capture a certain number of bytes per alert (due to storage space), so almost every packet is cut short,</p></blockquote><p>A packet in a pcap or pcapng file (or other file formats that support a snapshot length) has two lengths - "length on the network" and "amount of data saved". A program that's not saving all the bytes of the packets it captures should give the full length of the packet as the "length on the network" and the number of bytes it actually saved as "amount of data saved"; if it does so, that will <em>NOT</em> cause a "The capture file appears to have been cut short in the middle of a packet." error.</p><p>If, however, it writes out the full length of the packet as "amount of data saved", even though it doesn't actually save that many bytes, that file will be badly damaged to the point of unreadability, so that's presumably not what's happening here.</p><p>So there's "cut short" in the sense I described above, and there's "cut short" in the sense of the "The capture file appears to have been cut short in the middle of a packet." error; the two are different.</p><p>The "The capture file appears to have been cut short in the middle of a packet." error means that there's less data in the file for a packet than the "amount of data saved" says should be there, or that there isn't even a complete packet <em>record header</em> for the packet (the record header for a pcap file has the time stamp, the "length on the network", and the "amount of data saved"; for a pcapng file, it contains that information plus other information). <em>That's</em> the error you're getting.</p><p>And, as I have indicated, it is an <em>error</em>, not a <em>warning</em>, so there's no good reason to disable it.</p><p>If you're getting that error, the intrusion detection system you're using is failing to write out the entire record for the last packet; either it has a bug (as programs should <em>not</em> do that; they can, as I indicated, write out partial packet contents, but they must write out <em>all</em> of that partial content) or it's just running out of disk space.</p></div><div id="comment-55733-info" class="comment-info"><span class="comment-age">(21 Sep '16, 15:09)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-55728" class="comment-tools"></div><div class="clear"></div><div id="comment-55728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

