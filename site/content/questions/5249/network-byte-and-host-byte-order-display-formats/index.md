+++
type = "question"
title = "Network Byte and Host Byte Order Display formats"
description = '''Hi, I have been facing this issue for a very long time. I have a field (an integer) which is 00 00 24 20 in the byte stream. When I try to display it as decimal in my dissector, it shoes an incorrect value. That is because I want the dissector to take the value as 02 24 00 00 instead. Basically, I w...'''
date = "2011-07-26T04:43:00Z"
lastmod = "2011-07-27T07:39:00Z"
weight = 5249
keywords = [ "dissector", "display" ]
aliases = [ "/questions/5249" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Network Byte and Host Byte Order Display formats](/questions/5249/network-byte-and-host-byte-order-display-formats)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5249-score" class="post-score" title="current number of votes">0</div><span id="post-5249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have been facing this issue for a very long time. I have a field (an integer) which is 00 00 24 20 in the byte stream. When I try to display it as decimal in my dissector, it shoes an incorrect value. That is because I want the dissector to take the value as 02 24 00 00 instead. Basically, I want the reverse order.</p><p>How to display in that way?? How to use htonl/ntohl etc in the code.</p><p>Help Please..!!!</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/dbf35370bedfda8272cbf9e044a6cf1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sidharth&#39;s gravatar image" /><p><span>sidharth</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sidharth has no accepted answers">0%</span></p></div></div><div id="comments-container-5249" class="comments-container"></div><div id="comment-tools-5249" class="comment-tools"></div><div class="clear"></div><div id="comment-5249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5257"></span>

<div id="answer-container-5257" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5257-score" class="post-score" title="current number of votes">0</div><span id="post-5257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From doc/README.developer:</p><p><code>guint16 tvb_get_letohs(tvbuff_t*, gint offset);</code></p><p><code>guint32 tvb_get_letoh24(tvbuff_t*, gint offset);</code></p><p><code>guint32 tvb_get_letohl(tvbuff_t*, gint offset);</code></p><p><code>guint64 tvb_get_letoh40(tvbuff_t*, gint offset);</code></p><p><code>guint64 tvb_get_letoh48(tvbuff_t*, gint offset);</code></p><p><code>guint64 tvb_get_letoh56(tvbuff_t*, gint offset);</code></p><p><code>guint64 tvb_get_letoh64(tvbuff_t*, gint offset);</code></p><p>Also: see the final 'encoding' argument of <code>proto_tree_add_item()</code> as described in README.developer</p><p>Note well (again from README.developer):</p><p>Don't fetch a little-endian value using "tvb_get_ntohs() or "tvb_get_ntohl()" and then using "g_ntohs()", "g_htons()", "g_ntohl()", or "g_htonl()" on the resulting value - the g_ routines in question convert between network byte order (big-endian) and <em>host</em> byte order, not <em>little-endian</em> byte order; not all machines on which Wireshark runs are little-endian, even though PCs are. Fetch those values using "tvb_get_letohs()" and "tvb_get_letohl()".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-5257" class="comments-container"><span id="5298"></span><div id="comment-5298" class="comment"><div id="post-5298-score" class="comment-score"></div><div class="comment-text"><p>Hi Bill, Thanks for the reply but not all my problems were solved, unfortunately :(</p><p>I have a field as size with byte stream showing 03 00 00 00. It is a unsigned integer. In my code I donot apply any transformation on it. I just register in the function as FT_UINT32 and display as BASE_DEC. When I use proto_tree_add_item to add it to the tree (Encoding as False) it shows up as 3. Which is great as I have 3 nodes in the cluster. So that part is fine.</p><p>Next I want to display these nodes in a loop (one by one). So I use a loop like</p><p>while(i &lt; size)</p><p>There size value is not taken as 3 but intead as some huge number it seems.</p><p>So I applied : size = tvb_get_letohl(tvb,offset);</p><p>size=g_ntohl(size);</p><p>and then I am using size in the while loop hoping that its value is taken as 3.</p><p>But it does not work still.</p><p>Please HELP here..!! URGENT..!!!</p><p>Sidharth</p></div><div id="comment-5298-info" class="comment-info"><span class="comment-age">(27 Jul '11, 01:38)</span> <span class="comment-user userinfo">sidharth</span></div></div><span id="5301"></span><div id="comment-5301" class="comment"><div id="post-5301-score" class="comment-score"></div><div class="comment-text"><p>Skip the size=g_ntohl(size); That is what the note Bill quoted told you NOT to do.</p></div><div id="comment-5301-info" class="comment-info"><span class="comment-age">(27 Jul '11, 02:05)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="5313"></span><div id="comment-5313" class="comment"><div id="post-5313-score" class="comment-score"></div><div class="comment-text"><p>If you're using FALSE with proto_tree_add_item(i.e., specifying Big-Endian aka Network-Order) and the value displays as "3" then I'm confused.</p><p>A "byte stream" of "03 00 00 00" treated as Big-Endian will <em>not</em> display as "3". Are you using the correct offset when accessing the field ?</p></div><div id="comment-5313-info" class="comment-info"><span class="comment-age">(27 Jul '11, 07:39)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-5257" class="comment-tools"></div><div class="clear"></div><div id="comment-5257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

