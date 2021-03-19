+++
type = "question"
title = "DumpCap: Quotes Within Quotes?"
description = '''It finally dawned on me that DumpCap was the workaround for the memory situation. But I am having trouble concocting my filter argument. To wit (you have to scroll all the way to the right to see the offending argument): C:&#92;BAT&amp;gt;&quot;C:&#92;Program Files&#92;Wireshark&#92;dumpcap.exe&quot; -w &#92;&#92;NAS&#92;Temp&#92;DumpCap.pcap -...'''
date = "2011-02-21T17:21:00Z"
lastmod = "2011-02-21T19:20:00Z"
weight = 2462
keywords = [ "syntax" ]
aliases = [ "/questions/2462" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [DumpCap: Quotes Within Quotes?](/questions/2462/dumpcap-quotes-within-quotes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2462-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It finally dawned on me that DumpCap was the workaround for the memory situation.</p><p>But I am having trouble concocting my filter argument.</p><p>To wit (you have to scroll all the way to the right to see the offending argument):</p><pre><code>C:\BAT&gt;&quot;C:\Program Files\Wireshark\dumpcap.exe&quot; -w \\NAS\Temp\DumpCap.pcap  -i \Device\NPF_{35418EFA-22FB-4ADF-A88C-892918610B9F}  -f &quot;syslog.msg contains \&quot;INVITE sip:\&quot;&quot;
    Invalid capture filter: &quot;syslog.msg contains &quot;INVITE sip:&quot;&quot;!

    That string isn&#39;t a valid capture filter (syntax error).
    See the User&#39;s Guide for a description of the capture filter syntax.</code></pre><p>Seems like the quotes are resolving as expected, just that DumpCap isn't buying it.</p></div><div id="question-tags" class="tags-container tags">syntax</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '11, 17:21</strong></p><img src="https://secure.gravatar.com/avatar/8bde5a113e61480e8111dcc2e49409f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeteCress&#39;s gravatar image" /><p>PeteCress<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeteCress has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '11, 17:40</p></div></div><div id="comments-container-2462" class="comments-container"></div><div id="comment-tools-2462" class="comment-tools"></div><div class="clear"></div><div id="comment-2462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2464"></span>

<div id="answer-container-2464" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2464-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>dumpcap -f requires a <strong>capture</strong> filter (not a display filter).</p><p>See: http://wiki.wireshark.org/CaptureFilters</p><p>I don't think it's possible to do a string search with a capture filter;</p><p>Maybe you can use a capture filter (by ip address/port or whatever) to limit the traffic captured with dumpcap and then apply the display filter when you read the capture file with wireshark/tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '11, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-2464" class="comments-container"><span id="2475"></span><div id="comment-2475" class="comment"><div id="post-2475-score" class="comment-score"></div><div class="comment-text"><p>Bingo!</p><p>Capture Filter: -f "src net 10.0.0.4" Display Filter: syslog.msg contains "INVITE sip:"</p><p>Thanks.</p></div><div id="comment-2475-info" class="comment-info"><span class="comment-age">(22 Feb '11, 05:46)</span> PeteCress</div></div><span id="2478"></span><div id="comment-2478" class="comment"><div id="post-2478-score" class="comment-score"></div><div class="comment-text"><p>To put a finer point on it:</p><pre><code>:* =======================================================================
:* PURPOSE: To capture network traffic from VOIP adapter and then show
:*          same using WireShark to open the capture file.
:* =======================================================================

@ECHO OFF

ECHO .
ECHO Ctl-C, then reply &quot;N&quot; to stop and view
ECHO .

CD &quot;C:\Program Files\WireShark

SET DumpLoc=\\NAS\Temp\DumpCap.pcap

dumpcap.exe -w %DumpLoc%  -i \Device\NPF_{35418EFA-22FB-4ADF-A88C-892918610B9F}  -f &quot;src net 10.0.0.4&quot;

WireShark.exe -r %DumpLoc%  -R &quot;syslog.msg contains \&quot;INVITE sip:\&quot; and syslog.msg contains \&quot;Proxy\&quot;&quot;</code></pre></div><div id="comment-2478-info" class="comment-info"><span class="comment-age">(22 Feb '11, 06:30)</span> PeteCress</div></div><span id="39941"></span><div id="comment-39941" class="comment"><div id="post-39941-score" class="comment-score"></div><div class="comment-text"><p>Excellent, Thanks very much :)</p></div><div id="comment-39941-info" class="comment-info"><span class="comment-age">(19 Feb '15, 03:20)</span> Bumpudll3</div></div></div><div id="comment-tools-2464" class="comment-tools"></div><div class="clear"></div><div id="comment-2464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

