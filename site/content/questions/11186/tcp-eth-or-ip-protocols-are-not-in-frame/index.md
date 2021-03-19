+++
type = "question"
title = "TCP eth or IP protocols are not in frame"
description = '''Hi,  I&#x27;m trying to capture some http traffic from a machine&#x27;s local interface. So I run a command as such  tshark -i 1 -R data -V -l  The frames I get are like this Frame 18: 531 bytes on wire (4248 bits), 531 bytes captured (4248 bits)  Arrival Time: May 21, 2012 15:15:13.311786000 Eastern Daylight...'''
date = "2012-05-21T12:54:00Z"
lastmod = "2012-05-24T06:58:00Z"
weight = 11186
keywords = [ "capture", "troubleshooting" ]
aliases = [ "/questions/11186" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP eth or IP protocols are not in frame](/questions/11186/tcp-eth-or-ip-protocols-are-not-in-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11186-score" class="post-score" title="current number of votes">0</div><span id="post-11186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to capture some http traffic from a machine's local interface. So I run a command as such</p><blockquote><p><code>tshark -i 1 -R data -V -l</code></p></blockquote><p>The frames I get are like this</p><pre><code>Frame 18: 531 bytes on wire (4248 bits), 531 bytes captured (4248 bits)
    Arrival Time: May 21, 2012 15:15:13.311786000 Eastern Daylight Time
    Epoch Time: 1337627713.311786000 seconds
    [Time delta from previous captured frame: 0.009366000 seconds]
    [Time delta from previous displayed frame: 0.009366000 seconds]
    [Time since reference or first frame: 19.356632000 seconds]
    Frame Number: 18
    Frame Length: 531 bytes (4248 bits)
    Capture Length: 531 bytes (4248 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: data]</code></pre><p>As you can see the <code>eth:ip:tcp</code> information is not in frame. Does anyone know why? This is a VMware machine sniffing on the local interface. Could the fact that it's VMware be the problem? We've never seen this before even on VM machines.</p><p>Thanks,<br />
Al</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '12, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/c6ad098816c0b0afd0415f75e76ef68d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aaghili&#39;s gravatar image" /><p><span>aaghili</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aaghili has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '12, 14:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11186" class="comments-container"><span id="11188"></span><div id="comment-11188" class="comment"><div id="post-11188-score" class="comment-score"></div><div class="comment-text"><p>it works on my systems (tshark 1.6.7). What is your version?</p><blockquote><p><code>tshark -v</code></p></blockquote></div><div id="comment-11188-info" class="comment-info"><span class="comment-age">(21 May '12, 13:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11191"></span><div id="comment-11191" class="comment"><div id="post-11191-score" class="comment-score"></div><div class="comment-text"><p>Sure here is the -v info. I've also included the interface -D option and also the machine info. Thanks in advance.</p><pre><code>C:\Program Files\Wireshark&gt;tshark -v
TShark 1.6.7 (SVN Rev 41973 from /trunk-1.6)

Copyright 1998-2012 Gerald Combs &lt;[email protected]wireshark.org&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Compiled (64-bit) with GLib 2.26.1, with WinPcap (version unknown), with libz
without Kerberos, with GeoIP.
Running on 64-bit Windows Server 2008 Service Pack 2, build 6002,</code></pre></div><div id="comment-11191-info" class="comment-info"><span class="comment-age">(21 May '12, 14:45)</span> <span class="comment-user userinfo">aaghili</span></div></div><span id="11192"></span><div id="comment-11192" class="comment"><div id="post-11192-score" class="comment-score"></div><div class="comment-text"><pre><code>C:\Program Files\Wireshark&gt;tshark -D
1. \Device\NPF_{FABA2F2D-B86F-4923-9198-581F20F659A1} (VMware vmxnet3 virtual network device)
2. \Device\NPF_{3CC06A28-A9F7-4B31-8242-6F4D53CBF6FF} (MS Tunnel Interface Driver)</code></pre></div><div id="comment-11192-info" class="comment-info"><span class="comment-age">(21 May '12, 14:46)</span> <span class="comment-user userinfo">aaghili</span></div></div><span id="11199"></span><div id="comment-11199" class="comment"><div id="post-11199-score" class="comment-score"></div><div class="comment-text"><p>could be a problem with windows 2008. The same version (1.6.7) works as expected on my Windows XP test system. What happens if you run this command:</p><blockquote><p><code>tshark -i 1 -V -l</code></p></blockquote></div><div id="comment-11199-info" class="comment-info"><span class="comment-age">(21 May '12, 23:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11311"></span><div id="comment-11311" class="comment"><div id="post-11311-score" class="comment-score"></div><div class="comment-text"><p>This works for me as well. It also works with -T Fields option. But when I use -R data I don't see the TCP/IP ETH headers in the frame. I can get around this issue by using the other options but its strange that -R data option is not working correctly.</p></div><div id="comment-11311-info" class="comment-info"><span class="comment-age">(24 May '12, 06:58)</span> <span class="comment-user userinfo">aaghili</span></div></div></div><div id="comment-tools-11186" class="comment-tools"></div><div class="clear"></div><div id="comment-11186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

