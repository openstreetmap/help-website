+++
type = "question"
title = "Changing Defaults"
description = '''We are running sip and RTP stream captures that are being sent to a Windows capture server using 10 Gig Fiber. This is the only thing we are using it for. What we are finding is there seems to be no way to change the defaults. For example, in Help - About Wireshare - Folders, the default for &quot;File&quot; ...'''
date = "2011-01-13T10:17:00Z"
lastmod = "2011-01-19T07:47:00Z"
weight = 1739
keywords = [ "capture-filter", "settings" ]
aliases = [ "/questions/1739" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Changing Defaults](/questions/1739/changing-defaults)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1739-score" class="post-score" title="current number of votes">0</div><span id="post-1739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are running sip and RTP stream captures that are being sent to a Windows capture server using 10 Gig Fiber. This is the only thing we are using it for. What we are finding is there seems to be no way to change the defaults. For example, in Help - About Wireshare - Folders, the default for "File" dialogs, goes to "My Documents" folder. Is there a file that can be modified in Wireshark to change this directory? If no, is there an environmental variable we can change in windows that would allow this directory to change on startup?</p><p>Second question, Since we are doing SIP/RTP captures, we select are selecting the same options every time in the Wireshark Capture Options window. I can modify the Capture and Display options in the C:Documents and SettingsxxxApplication DataWiresharkpreferences file, but additionally I would like the Capture Filter to default to "udp port 5060", I would always want the capture file to be named capture.cap and default to a different directory than "My Documents" in windows. Lastly, I always want "Use multiple files" selected and "Next file ever" checked and defaulted to 100 megabytes and Ring buffer unselected. Is there any way to accomplish any of this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-settings" rel="tag" title="see questions tagged &#39;settings&#39;">settings</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '11, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/69e3947c8153fa38c10073bb1d54679e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmatthews0104&#39;s gravatar image" /><p><span>pmatthews0104</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmatthews0104 has no accepted answers">0%</span></p></div></div><div id="comments-container-1739" class="comments-container"></div><div id="comment-tools-1739" class="comment-tools"></div><div class="clear"></div><div id="comment-1739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1740"></span>

<div id="answer-container-1740" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1740-score" class="post-score" title="current number of votes">0</div><span id="post-1740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you might consider doing your captures through the command line tool <strong>dumpcap.exe</strong> instead of running Wireshark (which calls dumpcap when starting a capture anyway, passing a couple of parameters to it depending on your capture options dialog settings). If I were you I'd write a small script that calls dumpcap with your favorite parameters. That would also reduce overhead on the capture system because it can fully concentrate on receiving frames and writing them to disk.</p><p>Dumpcap.exe is installed with Wireshark in the same directory as the wireshark.exe. If you call it with <strong>dumpcap.exe -h</strong> you'll get a list of all parameters, and basically all you want to do is possible using those.</p><p>An example (which I admit I haven't tested, just to give you an idea) would be:</p><p><strong>dumpcap -f "udp port 5060" -w &lt;pathyouwant&gt;capture.cap -b filesize:100000000</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1740" class="comments-container"><span id="1750"></span><div id="comment-1750" class="comment"><div id="post-1750-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, I'll give that a try</p></div><div id="comment-1750-info" class="comment-info"><span class="comment-age">(14 Jan '11, 07:30)</span> <span class="comment-user userinfo">pmatthews0104</span></div></div></div><div id="comment-tools-1740" class="comment-tools"></div><div class="clear"></div><div id="comment-1740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1789"></span>

<div id="answer-container-1789" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1789-score" class="post-score" title="current number of votes">0</div><span id="post-1789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here's the batch file I came up with if anyone is interested in any of the pieces of it. Basically, it cleans out a directory, then starts a sip capture for udp port 5060. From there, you plug in a phone number and wireshark will fire up using a Display filter of the phone number variable you entered. This allows you to find an RTP port associated with a SIP invite. Then when you close out wireshark, you go back to the command prompt and enter in the udp port of the RTP stream you are looking for. It will then fire up a live capture of the RTP stream.</p><p>ECHO OFF</p><p>CLS</p><p>ECHO Moving Any Existing Files in "G:SIP Captures" to "G:SIP CapturesArchive"</p><p>ECHO.</p><p>ECHO.</p><p>Explorer "G:Sip Captures"</p><p>move /Y "G:SIP Captures*.*" "G:SIP CapturesArchive"</p><p>cd "G:SIP Captures"</p><p>ECHO.</p><p>ECHO.</p><p>ECHO Hit any Key to Start Capturing</p><p>ECHO.</p><p>pause</p><p>START "Wireshark" "C:Program FilesWiresharkdumpcap.exe" -i DeviceNPF_{E4E0896B-49C1-4945-B3A6- C094D9548B6C} -f "udp port 5060" -w "G:SIP CapturesSIP.cap" -b filesize:10000000</p><p>G:</p><p>pause</p><p>CLS</p><p>setLocal EnableDelayedExpansion</p><p>for /F %%a in ('dir /b *.cap') do (</p><p>set str=%%a</p><p>set Filename=%%a</p><p>)</p><p>c:</p><p>cd \</p><p>ECHO.</p><p>ECHO.</p><p>ECHO Type The Phone Number You're Looking for</p><p>ECHO.</p><p>ECHO.</p><p>ECHO ...............................................</p><p>ECHO.</p><p>ECHO Put the phone number in this format: 1555XXXXXXX</p><p>ECHO.</p><p>ECHO ...............................................</p><p>ECHO.</p><p>ECHO.</p><p>SET /P Phone=Phone Number is:</p><p>ECHO %Phone%</p><p>cd "c:Program FilesWireshark"</p><p>wireshark.exe -r "G:SIP Captures%Filename%" -R "sip.msg_hdr contains %Phone% and sip.Request-Line contains INVITE"</p><p>pause</p><p>ECHO.</p><p>ECHO Enter the UDP Port from SIP - Message Body - Media Description</p><p>ECHO.</p><p>SET /P UDP=UDP Port is:</p><p>START "Wireshark" "C:Program FilesWiresharkwireshark.exe" -i DeviceNPF_{E4E0896B-49C1-4947-B3A6-C094D9544B8A} -f "udp port %UDP%" -w "G:SIP CapturesRTP.cap" -b filesize:10000000 -k</p><p>pause</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '11, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/69e3947c8153fa38c10073bb1d54679e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmatthews0104&#39;s gravatar image" /><p><span>pmatthews0104</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmatthews0104 has no accepted answers">0%</span></p></div></div><div id="comments-container-1789" class="comments-container"><span id="1790"></span><div id="comment-1790" class="comment"><div id="post-1790-score" class="comment-score"></div><div class="comment-text"><p>Nice. Just a little comment: your executable paths are lacking one backslash between the Wireshark directory and the actual executable. I'm pretty sure that they were in your copy&amp;paste, but the message formatter "stole" it because it's used as an escape char. Try editing your code and replace the backslash with double backslashes, I think that should work.</p></div><div id="comment-1790-info" class="comment-info"><span class="comment-age">(18 Jan '11, 06:26)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-1789" class="comment-tools"></div><div class="clear"></div><div id="comment-1789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1812"></span>

<div id="answer-container-1812" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1812-score" class="post-score" title="current number of votes">0</div><span id="post-1812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Strange, they were in the script when I copied them. Not sure why they didn't show up on the board. Does the board allow / characters? Anyway, thanks for the note.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '11, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/69e3947c8153fa38c10073bb1d54679e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmatthews0104&#39;s gravatar image" /><p><span>pmatthews0104</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmatthews0104 has no accepted answers">0%</span></p></div></div><div id="comments-container-1812" class="comments-container"><span id="1813"></span><div id="comment-1813" class="comment"><div id="post-1813-score" class="comment-score"></div><div class="comment-text"><p>Oops, meant to do a backslash. Trying now.... \</p></div><div id="comment-1813-info" class="comment-info"><span class="comment-age">(19 Jan '11, 07:47)</span> <span class="comment-user userinfo">pmatthews0104</span></div></div></div><div id="comment-tools-1812" class="comment-tools"></div><div class="clear"></div><div id="comment-1812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

