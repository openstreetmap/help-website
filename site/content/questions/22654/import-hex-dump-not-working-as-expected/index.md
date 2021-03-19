+++
type = "question"
title = "Import hex dump not working as expected"
description = '''Hello, I have created a TCL script that creates a text file containing a wireshark hex dump. The text file consists of multiple lines similar to this one: 000000 90 b1 1c 99 53 f5 00 18 19 b5 86 44 08 00 4D FE 04 08 E7 5C 1B  This is just the beginning of a line, it contains a TCP packet encapsulate...'''
date = "2013-07-04T07:13:00Z"
lastmod = "2013-07-08T01:50:00Z"
weight = 22654
keywords = [ "import", "hex", "dump", "wireshark" ]
aliases = [ "/questions/22654" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Import hex dump not working as expected](/questions/22654/import-hex-dump-not-working-as-expected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22654-score" class="post-score" title="current number of votes">0</div><span id="post-22654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have created a TCL script that creates a text file containing a wireshark hex dump.</p><p>The text file consists of multiple lines similar to this one:</p><pre><code>000000 90 b1 1c 99 53 f5 00 18 19 b5 86 44 08 00 4D FE 04 08 E7 5C 1B</code></pre><p>This is just the beginning of a line, it contains a TCP packet encapsulated with IPv4 and then ethernet. I'd like to import my file to Wireshark and analyze it there, but when I do this, something odd happens.</p><p>Wireshark detects every line as a single packet, detects and analyses correct the information in the IPv4 and Ethernet headers, however the IPv4 payload that is supposed to be a TCP encapsulation is not loaded into Wireshark (the "Data" section of the IPv4 datagram is detected as being of 12 bytes length.).</p><p>I hope i have been explicit enough and that someone could help me :)</p><p>Thank you very much!</p><p>Extra information:</p><p>I managed to figure out why the data wasn't all loaded (had something wrong in the TCL script).</p><p>However, I stumbled upon something else.</p><p>Wireshark detects the payload of the IPv4 header as "data" instead of a TCP packet. I thought this happened before only because he was loading only 12 bytes of data.</p><p>This is an input file example: <a href="http://pastebin.com/uXY8tN52">http://pastebin.com/uXY8tN52</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/b68fad6a138a4a8e90f659020ff5b705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maio&#39;s gravatar image" /><p><span>Maio</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '13, 00:51</strong> </span></p></div></div><div id="comments-container-22654" class="comments-container"><span id="22655"></span><div id="comment-22655" class="comment"><div id="post-22655-score" class="comment-score"></div><div class="comment-text"><p>please add more lines of the actual input</p></div><div id="comment-22655-info" class="comment-info"><span class="comment-age">(04 Jul '13, 07:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22662"></span><div id="comment-22662" class="comment"><div id="post-22662-score" class="comment-score"></div><div class="comment-text"><blockquote><p>4D FE 04 08 E7 5C 1B</p></blockquote><p>OK, so that's:</p><ul><li><code>4D</code> - version 4, header length 13*4 = 52 bytes</li><li><code>FE</code> - type of service</li><li><code>04 08</code> - total length, 1032 bytes</li><li><code>E7 5C</code> - identification</li><li><code>1B</code> - first byte of flags+fragment offset, so this isn't the first fragment</li></ul><p>so <em>that</em> packet shouldn't be dissected as TCP unless you have the rest of the fragments.</p><p>Please give <em>all</em> the lines of at least one packet that's not being dissected as you expect.</p></div><div id="comment-22662-info" class="comment-info"><span class="comment-age">(04 Jul '13, 09:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-22654" class="comment-tools"></div><div class="clear"></div><div id="comment-22654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22708"></span>

<div id="answer-container-22708" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22708-score" class="post-score" title="current number of votes">1</div><span id="post-22708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Maio has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Wireshark detects the payload of the IPv4 header as "data" instead of a TCP packet. I thought this happened before only because he was loading only 12 bytes of data. This is an input file example: <a href="http://pastebin.com/uXY8tN52">http://pastebin.com/uXY8tN52</a></p></blockquote><p>Your TCL script is still not working correctly. The IP V4 header contains different flags and values, that should not be there (at least that's what I think, without knowing your data).</p><p>I recommend to check at least the <strong><a href="http://de.wikipedia.org/wiki/DiffServ">DiffServ</a></strong> fields and the <strong>Fragemt offset</strong>. If I set those values to 0x00, I get at least something that looks like <strong>parts</strong> of a TCP frame (still not correct).</p><p>Then there are some $ signs in the text like $E and $5. Please fix that as well.</p><p>If think the script needs some more tweaking. Where do you get the packet data from?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '13, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '13, 02:02</strong> </span></p></div></div><div id="comments-container-22708" class="comments-container"></div><div id="comment-tools-22708" class="comment-tools"></div><div class="clear"></div><div id="comment-22708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22680"></span>

<div id="answer-container-22680" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22680-score" class="post-score" title="current number of votes">0</div><span id="post-22680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since you say that Wireshark reads every line as its own packet, from that I think you're TCL script is most likely (as suggested) using an all-zero offset for each line. Is that the case? How are you building those offsets?</p><p>I haven't touched a TCL script in years but if it helps this is how I build those hex offsets in perl, into a format that Wireshark will accept. In this loop, each entry in the "<span><span>@packets</span></span>" array is a packet in hexidecimal form:</p><p><code>foreach (@packets) {         $packet = $_;         $packet_length = $_ =~ tr/[0-9a-zA-Z]//;         # The +0.999... is a cheap way to round up for the last line.         $line_count = int(($packet_length/32) + 0.9999999999);         for ($n=0; $n &lt; $line_count; $n++){             $offset = sprintf("%x",($n*16));             # Assumes no offset greater than 4 hex characters.             $lead_zeros = 4 - ($offset =~ tr/[0-9a-zA-Z]//);             $lead_zeros = '0' x $lead_zeros;             $bytes = substr($packet,$n*32,32);             # Adds a space character after every byte.             $bytes =~ s/([0-9a-zA-Z]{2})/$1 /g;             print "$lead_zeros$offset  $bytes\n";         } }</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '13, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jul '13, 16:04</strong> </span></p></div></div><div id="comments-container-22680" class="comments-container"></div><div id="comment-tools-22680" class="comment-tools"></div><div class="clear"></div><div id="comment-22680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

