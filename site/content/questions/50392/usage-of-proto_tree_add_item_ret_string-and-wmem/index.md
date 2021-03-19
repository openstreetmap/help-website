+++
type = "question"
title = "Usage of proto_tree_add_item_ret_string() and WMEM"
description = '''Hi, I&#x27;ve been trying to use the following function to add some decoded text to a colum with the col_add_fstr() function. WS_DLL_PUBLIC proto_item * proto_tree_add_item_ret_string(proto_tree *tree, int hfindex, tvbuff_t *tvb, const gint start, gint length, const guint encoding, wmem_allocator_t *scop...'''
date = "2016-02-22T02:14:00Z"
lastmod = "2016-02-23T15:12:00Z"
weight = 50392
keywords = [ "proto_item", "memory" ]
aliases = [ "/questions/50392" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Usage of proto\_tree\_add\_item\_ret\_string() and WMEM](/questions/50392/usage-of-proto_tree_add_item_ret_string-and-wmem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50392-score" class="post-score" title="current number of votes">0</div><span id="post-50392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've been trying to use the following function to add some decoded text to a colum with the col_add_fstr() function.</p><pre><code>WS_DLL_PUBLIC proto_item * proto_tree_add_item_ret_string(proto_tree *tree, int hfindex, tvbuff_t *tvb, const gint start, gint length, const guint encoding, wmem_allocator_t *scope, const guint8 **retval);</code></pre><p>I've read README.wmem, but still, I don't understand how to simply return the decoded string.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_item" rel="tag" title="see questions tagged &#39;proto_item&#39;">proto_item</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '16, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/46ef36ddea155cb13d6344c0c1731b7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_michel&#39;s gravatar image" /><p><span>_michel</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_michel has no accepted answers">0%</span></p></div></div><div id="comments-container-50392" class="comments-container"></div><div id="comment-tools-50392" class="comment-tools"></div><div class="clear"></div><div id="comment-50392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50394"></span>

<div id="answer-container-50394" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50394-score" class="post-score" title="current number of votes">2</div><span id="post-50394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-rdp.c;h=52e0d8bf93bc7686027fb9655386ea57048cb76c;hb=HEAD">rdp dissector</a> uses the function, around line 2161 if that helps.</p><p>You haven't really described your issue, please amend your question to show how you're attempting to call the function from your code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '16, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '17, 06:49</strong> </span></p></div></div><div id="comments-container-50394" class="comments-container"><span id="50406"></span><div id="comment-50406" class="comment"><div id="post-50406-score" class="comment-score"></div><div class="comment-text"><p>Thank you, it works. In case someone is interested, I paste here the relevant lines :</p><pre><code>static int
dissect_rdp_cr(tvbuff_t *tvb, packet_info *pinfo, proto_tree *parent_tree, void* data _U_)
{
    ...
    const guint8 *stringval;
    ...
    proto_tree_add_item_ret_string(tree, hf_rdp_rt_cookie, tvb, offset,
                                   linelen, ENC_ASCII|ENC_NA,
                                   wmem_packet_scope(), &amp;stringval);
    ...
}</code></pre><p>with the following declaraction in wmem_scopes.h</p><pre><code>WS_DLL_PUBLIC
wmem_allocator_t *
wmem_packet_scope(void);</code></pre></div><div id="comment-50406-info" class="comment-info"><span class="comment-age">(22 Feb '16, 07:41)</span> <span class="comment-user userinfo">_michel</span></div></div></div><div id="comment-tools-50394" class="comment-tools"></div><div class="clear"></div><div id="comment-50394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50421"></span>

<div id="answer-container-50421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50421-score" class="post-score" title="current number of votes">0</div><span id="post-50421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I don't understand how to simply return the decoded string.</p></blockquote><p>How long do you need the string to last? That determines the scope to pass to <code>proto_tree_add_item_ret_string()</code>. If you only need it to use within the dissector call, <code>wmem_packet_scope()</code> is, in fact, the right answer. If its value needs to persist past the end of dissection, you'd need a different scope.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '16, 16:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Feb '16, 17:00</strong> </span></p></div></div><div id="comments-container-50421" class="comments-container"><span id="50427"></span><div id="comment-50427" class="comment"><div id="post-50427-score" class="comment-score"></div><div class="comment-text"><p>I don't know exactly, I just need it to be displayed in the column info. Since I don't know what and when is being freed by Wireshark, I can't tell the scope I need.</p><p>I've looked in README.wmem but I don't have the necessary experience to choose between packet, file or epan pool. Off the top of my head, I'd say that packet pool, hence wmem<em>packet</em>scope(), is ok. I'd need a clear example to understand the limitations of each pool.</p></div><div id="comment-50427-info" class="comment-info"><span class="comment-age">(22 Feb '16, 23:55)</span> <span class="comment-user userinfo">_michel</span></div></div><span id="50451"></span><div id="comment-50451" class="comment"><div id="post-50451-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I just need it to be displayed in the column info.</p></blockquote><p>Then you'll probably be doing <code>col_add_str()</code> or <code>col_add_fstr()</code>; neither of those routines keep copies of the string pointers passed to them, so they could be freed at any point, and <code>wmem_packet_scope()</code> would suffice.</p></div><div id="comment-50451-info" class="comment-info"><span class="comment-age">(23 Feb '16, 15:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-50421" class="comment-tools"></div><div class="clear"></div><div id="comment-50421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

