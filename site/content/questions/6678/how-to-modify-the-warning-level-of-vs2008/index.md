+++
type = "question"
title = "how to modify the warning level of vs2008"
description = '''Hi guys, Some warnings displayed when I compiled the Wireshark source code after modifying some code. Please see below: packet-ethertype.c(211) : error C2220: warning treated as error - no &#x27;object&#x27; file generated packet-ethertype.c(211) : warning C4029: declared formal parameter list different from ...'''
date = "2011-10-02T04:17:00Z"
lastmod = "2011-10-03T19:36:00Z"
weight = 6678
keywords = [ "development" ]
aliases = [ "/questions/6678" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to modify the warning level of vs2008](/questions/6678/how-to-modify-the-warning-level-of-vs2008)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6678-score" class="post-score" title="current number of votes">0</div><span id="post-6678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>Some warnings displayed when I compiled the Wireshark source code after modifying some code. Please see below:</p><pre><code>packet-ethertype.c(211) : error C2220: warning treated as error - no &#39;object&#39; file generated
packet-ethertype.c(211) : warning C4029: declared formal parameter list different from definition
packet-eth.c(434) : error C2220: warning treated as error - no &#39;object&#39; file generated
packet-eth.c(434) : warning C4020: &#39;ethertype&#39; : too many actual parameters
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>I've no idea where the problem is. I searched Google, and someone said the warning level of my VS2008 shouldn't be so high, but I didn't find anywhere how to modify the warning level. Anyone know how to modify this?</p><p>Thanks in advance!</p><p>Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '11, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/e9d668dd28830dd8f79d4dbb56e5f2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam&#39;s gravatar image" /><p><span>Sam</span><br />
<span class="score" title="51 reputation points">51</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '11, 15:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6678" class="comments-container"></div><div id="comment-tools-6678" class="comment-tools"></div><div class="clear"></div><div id="comment-6678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6679"></span>

<div id="answer-container-6679" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6679-score" class="post-score" title="current number of votes">2</div><span id="post-6679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>packet-ethertype.c(211) : error C2220: warning treated as error - no &#39;object&#39; file generated
packet-ethertype.c(211) : warning C4029: declared formal parameter list different from definition
packet-eth.c(434) : error C2220: warning treated as error - no &#39;object&#39; file generated
packet-eth.c(434) : warning C4020: &#39;ethertype&#39; : too many actual parameters</code></pre><p>The above two warnings need to be fixed. The messages should be self-explanatory.</p><p>Did you make changes to the definition of ethertype in packet-ethertype.c ?<br />
</p><p>If yes, your changes need work to solve the errors.</p><p>If not, does your Wireshark source w/o any of your changes compile w/o error ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '11, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '11, 06:21</strong> </span></p></div></div><div id="comments-container-6679" class="comments-container"><span id="6680"></span><div id="comment-6680" class="comment"><div id="post-6680-score" class="comment-score"></div><div class="comment-text"><p>thanks, Bill. I just have a parameter/vtime_id added in packet-ethertype.c as below:</p><p>ethertype(guint16 etype, tvbuff_t <em>tvb, int offset_after_etype, packet_info</em> pinfo, proto_tree <em>tree, proto_tree</em> fh_tree, int etype_id, int vtime_id, int trailer_id, int fcs_len)</p><p>Does this have some problem? anywhere else need to changed if theparameter/vtime_id added? BTW, why I added this parameter/vtime_id? because I have some bytes in the trailer need be extracted. For expample, if the trailer is: 112233445566778899, I want the first four bytes need be recongnized as 'vtime', and the last five bytes recognized as 'trailer'. Do you have any idea? Thanks again.</p></div><div id="comment-6680-info" class="comment-info"><span class="comment-age">(02 Oct '11, 08:18)</span> <span class="comment-user userinfo">Sam</span></div></div><span id="6681"></span><div id="comment-6681" class="comment"><div id="post-6681-score" class="comment-score">1</div><div class="comment-text"><p>Firstly you should have made your second entry a comment to Bill's answer, not an "answer" of your own.</p><p>Secondly, if you modify the function definition you must modify any corresponding function declaration, i.e. in epan/packet.h. This is the cause of the 'packet-ethertype.c(211) : warning C4029: declared formal parameter list different from definition' warning.</p><p>Thirdly, any code that calls your modified function must also be modified to match the modified function declaration. This is the cause of the 'packet-eth.c(434) : warning C4020: 'ethertype' : too many actual parameters' warning.</p></div><div id="comment-6681-info" class="comment-info"><span class="comment-age">(02 Oct '11, 13:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="6683"></span><div id="comment-6683" class="comment"><div id="post-6683-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", please see the FAQ for details)</p></div><div id="comment-6683-info" class="comment-info"><span class="comment-age">(02 Oct '11, 14:55)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="6685"></span><div id="comment-6685" class="comment"><div id="post-6685-score" class="comment-score"></div><div class="comment-text"><p>First line, I modified the epan/packet.h and then compiled success follow your tips. thank you, Grahamb.</p><p>But what's meaning about the word 'w/o' or w/o error in previous comment from Bill?</p><p>Sam</p></div><div id="comment-6685-info" class="comment-info"><span class="comment-age">(02 Oct '11, 19:56)</span> <span class="comment-user userinfo">Sam</span></div></div><span id="6686"></span><div id="comment-6686" class="comment"><div id="post-6686-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.thefreedictionary.com/w%2Fo">w/o</a> is an abbreviation for "without".</p></div><div id="comment-6686-info" class="comment-info"><span class="comment-age">(02 Oct '11, 20:04)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="6689"></span><div id="comment-6689" class="comment not_top_scorer"><div id="post-6689-score" class="comment-score"></div><div class="comment-text"><p>Thank you, helloworld. Thank you all for help. My reply is wireshark source have no any errors. And I have another question need your help.</p><p>I use the function 'proto_tree_add_item' to put some bytes to the 'vtime' item, but the bytes are just hex code, but its readability is very poor, I have to convert these bytes to a good readability format.</p><p>For example: The 'vtime' item display '64000064', and I need convert the '64000064' to '100.0.0.100' and displayed in the 'vtime' item. how to do it? use the 'vtime_id' like the 'trailer_id'?</p><p>thanks again.</p><p>Sam</p></div><div id="comment-6689-info" class="comment-info"><span class="comment-age">(03 Oct '11, 19:36)</span> <span class="comment-user userinfo">Sam</span></div></div></div><div id="comment-tools-6679" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-6679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

