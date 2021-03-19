+++
type = "question"
title = "pcap to raw hex dump"
description = '''I&#x27;m looking to convert pcap file to a raw dump of the bytes of the packets. This is when export file to txt file using wireshark  then the requirement data is only hex data in red box. Because packet data is too much, so need some script to implement this.  and this the result and create multiple fi...'''
date = "2011-01-26T13:13:00Z"
lastmod = "2011-02-27T23:28:00Z"
weight = 1950
keywords = [ "pcap-hex", "hexdump" ]
aliases = [ "/questions/1950" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [pcap to raw hex dump](/questions/1950/pcap-to-raw-hex-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1950-score" class="post-score" title="current number of votes">0</div><span id="post-1950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking to convert pcap file to a raw dump of the bytes of the packets.</p><p>This is when export file to txt file using wireshark <img src="http://lh6.ggpht.com/_jyfqq2mA0_I/TUCJZMH1pPI/AAAAAAAAABI/mzgiS-OJJxc/oringinal_txt.PNG" title="Original txt file" alt="alt text" /></p><p>then the requirement data is only hex data in red box. Because packet data is too much, so need some script to implement this. <img src="http://lh6.ggpht.com/_jyfqq2mA0_I/TUCJZZlwGBI/AAAAAAAAABM/NGIL7AkZLLc/hex_txt.PNG" title="requirement hex data" alt="alt text" /></p><p>and this the result and create multiple file depend on number of packet data<img src="http://lh4.ggpht.com/_jyfqq2mA0_I/TUCNjUH6CEI/AAAAAAAAABc/DgkaSenDnyU/hex_SD.PNG" title="final result" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap-hex" rel="tag" title="see questions tagged &#39;pcap-hex&#39;">pcap-hex</span> <span class="post-tag tag-link-hexdump" rel="tag" title="see questions tagged &#39;hexdump&#39;">hexdump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '11, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/9fc48c3dad2c050fd7a39711084dfc55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="faz&#39;s gravatar image" /><p><span>faz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="faz has no accepted answers">0%</span></p></img></div></div><div id="comments-container-1950" class="comments-container"></div><div id="comment-tools-1950" class="comment-tools"></div><div class="clear"></div><div id="comment-1950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1953"></span>

<div id="answer-container-1953" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1953-score" class="post-score" title="current number of votes">0</div><span id="post-1953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not entirely sure I understand what you're asking. If you want just the ASCII hex dump of all data and nothing else, then you can simply pipe the output of tshark through sed like so:</p><p><code>tshark -x -r mydata.pcap | sed -n 's/^[0-9a-f]*\s\(\(\s[0-9a-f][0-9a-f]\)\{1,16\}\).*$/\1/p'</code></p><p>If that's not what you're asking, perhaps you could clarify. I don't understand "create multiple file depend on number of packet data." Do you mean that you want to create one file per packet? Is the file to be a hex dump (printable form) or is it a pure binary file?<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '11, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p><span>beroset</span><br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Oct '13, 13:21</strong> </span></p></div></div><div id="comments-container-1953" class="comments-container"><span id="1978"></span><div id="comment-1978" class="comment"><div id="post-1978-score" class="comment-score"></div><div class="comment-text"><p>when i'm try using tshark thought sed..give some error:</p><p><em>'sed' is not recognized as an internal or external command, operable program or batch file.</em></p><p>yes,I just want hex data only and want to create one file per packet. In this picture (printable form) is not same file with above. That's is just some example only. But actually hex data will be same.</p></div><div id="comment-1978-info" class="comment-info"><span class="comment-age">(27 Jan '11, 11:32)</span> <span class="comment-user userinfo">faz</span></div></div><span id="2580"></span><div id="comment-2580" class="comment"><div id="post-2580-score" class="comment-score"></div><div class="comment-text"><p>You're probably running Windows; I'm not sure what commands that come with Windows would help here, but you might look at <a href="http://gnuwin32.sourceforge.net/packages/sed.htm">sed for Windows</a>.</p></div><div id="comment-2580-info" class="comment-info"><span class="comment-age">(27 Feb '11, 23:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1953" class="comment-tools"></div><div class="clear"></div><div id="comment-1953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2559"></span>

<div id="answer-container-2559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2559-score" class="post-score" title="current number of votes">0</div><span id="post-2559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>sed</code> command given above didn't work for me. I'm no <code>sed</code> expert so there's probably a better, more robust way to do this, but the following seemed to work for me, for what it's worth:</p><pre><code>tshark -x -r mydata.pcap | sed -n &#39;s/^[0-9a-f][0-9a-f]*  \(.*  \) .*/\1/p&#39;</code></pre><p>faz, since your system doesn't have <code>sed</code> installed, I can logically conclude that you are most likely working on Windows, so you will probably need to install <a href="http://www.cygwin.com/">cygwin</a> in order to have <code>sed</code> at your disposal. There may be some other "<code>sed</code> for Windows" alternatives if you don't want to install cygwin.</p><p>You can find more information on <code>sed</code> <a href="http://www.gnu.org/software/sed/manual/sed.html">here</a> or <a href="http://en.wikipedia.org/wiki/Sed">here</a> or at a number of other places.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '11, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></img></div></div><div id="comments-container-2559" class="comments-container"></div><div id="comment-tools-2559" class="comment-tools"></div><div class="clear"></div><div id="comment-2559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

