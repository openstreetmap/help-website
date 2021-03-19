+++
type = "question"
title = "how to get only the headers of a packet"
description = '''Hi, Is there any way to use display filters to get only the headers for a packet and not the contents/payload (e.g. which seem to follow the content-length header in SIP) using tshark. It is possible to select individual headers but I know not any way to exclude the payload. Thanks, qwerfdsa'''
date = "2013-03-12T21:01:00Z"
lastmod = "2016-02-23T06:17:00Z"
weight = 19411
keywords = [ "payload", "tshark", "display-filter" ]
aliases = [ "/questions/19411" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to get only the headers of a packet](/questions/19411/how-to-get-only-the-headers-of-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19411-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there any way to use display filters to get only the headers for a packet and not the contents/payload (e.g. which seem to follow the content-length header in SIP) using tshark. It is possible to select individual headers but I know not any way to exclude the payload.</p><p>Thanks, qwerfdsa</p></div><div id="question-tags" class="tags-container tags">payload tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 21:01</strong></p><img src="https://secure.gravatar.com/avatar/78fdb0b07eaa8e7ef156b2cc2a067252?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qwerfdsa&#39;s gravatar image" /><p>qwerfdsa<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qwerfdsa has no accepted answers">0%</span></p></div></div><div id="comments-container-19411" class="comments-container"></div><div id="comment-tools-19411" class="comment-tools"></div><div class="clear"></div><div id="comment-19411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="19429"></span>

<div id="answer-container-19429" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19429-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot do that with display filters. You could use "editcap -s" (editcap is a command line tool that comes with Wireshark) to cut away parts of each packet at a certain offset. That offset has to be the same for each packet, which means that if not all headers have the same size the cut will be in different parts of the packet.</p><p>Keep in mind that using editcap to cut away the parts means that they're not in the capture file anymore, so they cannot be restored unless you keep the original file as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19429" class="comments-container"></div><div id="comment-tools-19429" class="comment-tools"></div><div class="clear"></div><div id="comment-19429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19462"></span>

<div id="answer-container-19462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19462-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Get" in what sense?</p><p>Display filters can exclude entire packets from the display; they are not a mechanism to filter out parts of individual packets.</p><p>If you want to limit the contents of your capture file to the packet headers, see Jasper's answer - that is a bit of a crude tool, as it slices packets off at a fixed offset (it's the equivalent of "-s" in tcpdump/dumpcap/TShark/Wireshark and the "Limit each packet to XXX bytes" GUI option in Wireshark) rather than at a particular layer of the packet, but it may do what you want.</p><p>If you're trying to <em>extract</em> particular fields for processing in some other script or tool, see TShark's "-T fields" option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19462" class="comments-container"><span id="19469"></span><div id="comment-19469" class="comment"><div id="post-19469-score" class="comment-score"></div><div class="comment-text"><p>Since they seem to be \r\n separated, would it be possible to separate them using any regular expression supporting command line utility (Linux)?</p></div><div id="comment-19469-info" class="comment-info"><span class="comment-age">(13 Mar '13, 12:18)</span> qwerfdsa</div></div><span id="19470"></span><div id="comment-19470" class="comment"><div id="post-19470-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Since they seem to be \r\n separated</p></blockquote><p>What do you mean by "they"? Are you talking about the default output of <code>tshark -V</code>? Are you talking about the contents of a SIP message?</p></div><div id="comment-19470-info" class="comment-info"><span class="comment-age">(13 Mar '13, 12:25)</span> Guy Harris ♦♦</div></div><span id="19471"></span><div id="comment-19471" class="comment"><div id="post-19471-score" class="comment-score"></div><div class="comment-text"><p>Yes. From the RFC 3261, Response/Request= Status-Line*( message-header )CRLF[ message-body] So the contents seem to be separated from the headers by a CRLF.</p></div><div id="comment-19471-info" class="comment-info"><span class="comment-age">(13 Mar '13, 12:31)</span> qwerfdsa</div></div><span id="19472"></span><div id="comment-19472" class="comment"><div id="post-19472-score" class="comment-score"></div><div class="comment-text"><p>So how are you extracting the headers? Would you use the regex-supporting utility on:</p><ul><li>the output of <code>tshark -V</code>;</li><li>the output of <code>tshark -T fields -e</code>...;</li><li>the output of some other tool;</li><li>the raw capture file?</li></ul><p>I would <em>strongly</em> recommend against the latter, as capture files are binary files.</p></div><div id="comment-19472-info" class="comment-info"><span class="comment-age">(13 Mar '13, 13:28)</span> Guy Harris ♦♦</div></div><span id="19485"></span><div id="comment-19485" class="comment"><div id="post-19485-score" class="comment-score"></div><div class="comment-text"><p>I only have the raw capture file to experiment with. vim seems to render plaintext until the actual content and od indicates a \r\n between the headers and the content. How would I be able to use grep to separate them (using collations?) - Thanks</p></div><div id="comment-19485-info" class="comment-info"><span class="comment-age">(13 Mar '13, 17:50)</span> qwerfdsa</div></div></div><div id="comment-tools-19462" class="comment-tools"></div><div class="clear"></div><div id="comment-19462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50433"></span>

<div id="answer-container-50433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50433-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://stackoverflow.com/users/684451/joke">joke</a> on Stack Overflow came up with <a href="http://stackoverflow.com/a/32396230/2877364">this answer</a> in Wireshark, which worked for me. Joke's answer also has a <code>tshark</code> example.</p><ol><li>Apply a display filter, such as <code>sip</code></li><li>Go to the the Packet Details pane.</li><li>Expand "Session Initiation Protocol"</li><li>Expand Request-Line, Message Header and Message Body* (do not Expand Subtrees)</li><li>Go to File - Export - Export Packet Dissections... - As "Plain Text" File...</li><li>Packet Format section: select "Packet Summery Line" and "Packet Details: As Displayed"</li><li>Add a file name and save the file</li></ol><p>(<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA 3.0</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/0a101160e41fd7fd75f5fc701f8acb1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cxw&#39;s gravatar image" /><p>cxw<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cxw has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Feb '16, 06:18</p></div></div><div id="comments-container-50433" class="comments-container"></div><div id="comment-tools-50433" class="comment-tools"></div><div class="clear"></div><div id="comment-50433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

