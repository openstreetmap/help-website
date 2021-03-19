+++
type = "question"
title = "Old Style vs. New Style Dissector"
description = '''How does Wireshark determine the style of dissector (new or old) ? For example the code below, how is &quot;handle-&amp;gt;is_new&quot; true or false?  /* This function will return  * old style dissector :  * length of the payload or 1 of the payload is empty  * new dissector :  * &amp;gt;0 this protocol was successf...'''
date = "2015-05-13T12:15:00Z"
lastmod = "2015-05-13T12:47:00Z"
weight = 42377
keywords = [ "style", "type", "packet" ]
aliases = [ "/questions/42377" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Old Style vs. New Style Dissector](/questions/42377/old-style-vs-new-style-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42377-score" class="post-score" title="current number of votes">0</div><span id="post-42377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does Wireshark determine the style of dissector (new or old) ? For example the code below, how is "handle-&gt;is_new" true or false?</p><pre><code>    /* This function will return
 * old style dissector :
 *   length of the payload or 1 of the payload is empty
 * new dissector :
 *   &gt;0  this protocol was successfully dissected and this was this protocol.
 *   0   this packet did not match this protocol.
 *
 * The only time this function will return 0 is if it is a new style dissector
 * and if the dissector rejected the packet.
 */
call_dissector_through_handle(dissector_handle_t handle, tvbuff_t *tvb,
                  packet_info *pinfo, proto_tree *tree, void *data)
{

......

    if (handle-&gt;is_new) {
        EP_CHECK_CANARY((&quot;before calling handle-&gt;dissector.new_d for %s&quot;,handle-&gt;name));
        ret = (*handle-&gt;dissector.new_d)(tvb, pinfo, tree, data);
        EP_CHECK_CANARY((&quot;after calling handle-&gt;dissector.new_d for %s&quot;,handle-&gt;name));
    } else {
        EP_CHECK_CANARY((&quot;before calling handle-&gt;dissector.old for %s&quot;,handle-&gt;name));
subdissector */
        (*handle-&gt;dissector.old)(tvb, pinfo, tree);
        EP_CHECK_CANARY((&quot;after calling handle-&gt;dissector.old for %s&quot;,handle-&gt;name));
        ret = tvb_length(tvb);
        if (ret == 0) {
            /*
             * XXX - a tvbuff can have 0 bytes of data in
             * it, so we have to make sure we don&#39;t return
             * 0.
             */
            ret = 1;
        }</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '15, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/42f084d62348c04d00bd67b129116cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XQW1123&#39;s gravatar image" /><p><span>XQW1123</span><br />
<span class="score" title="46 reputation points">46</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XQW1123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '15, 12:17</strong> </span></p></div></div><div id="comments-container-42377" class="comments-container"></div><div id="comment-tools-42377" class="comment-tools"></div><div class="clear"></div><div id="comment-42377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42378"></span>

<div id="answer-container-42378" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42378-score" class="post-score" title="current number of votes">1</div><span id="post-42378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="XQW1123 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>handle-&gt;is_new is set depending on the function you call for the dissector registration: create_dissector_handle/register_dissector for old style and new_create_dissector_handle/new_register_dissector for new style.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-42378" class="comments-container"></div><div id="comment-tools-42378" class="comment-tools"></div><div class="clear"></div><div id="comment-42378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

