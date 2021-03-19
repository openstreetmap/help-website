+++
type = "question"
title = "How to use array fields in a dissector???"
description = '''I am writing a dissector for cluster heartbeat packets for NetScaler. I am facing an issue with a field named LVS. Actually it is a 4 byte integer. But it refers to a set of nodes in the view set. The set can be as big as 32.  So I have used the following code to show all the nodes in the LVS (from ...'''
date = "2011-07-13T07:02:00Z"
lastmod = "2011-07-22T06:41:00Z"
weight = 5020
keywords = [ "dissector" ]
aliases = [ "/questions/5020" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use array fields in a dissector???](/questions/5020/how-to-use-array-fields-in-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5020-score" class="post-score" title="current number of votes">0</div><span id="post-5020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector for cluster heartbeat packets for NetScaler. I am facing an issue with a field named LVS. Actually it is a 4 byte integer. But it refers to a set of nodes in the view set. The set can be as big as 32.</p><p>So I have used the following code to show all the nodes in the LVS (from the trace)</p><p>declare array variable - static int hf_hb_cl_lvs[32];</p><p>Register this array variable in the register function.</p><p>To display in the tree::</p><p>for(i=0; i&lt;31; i++) { if(hf_hb_cl_lvs[i] != 0x00000000) { proto_tree_add_item(.................parameters.................); } offset+=4; }</p><h6 id="section"></h6><p>The issue is that this piece of code adds only the first node from the byte stream to the tree in the display. It does not add any node beyond that.</p></h6><h6 id="section-1"></h6><p>Please help me with the code here??</p><p>Regards, Sidharth</p></h6></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '11, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p><span>sid</span><br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-5020" class="comments-container"></div><div id="comment-tools-5020" class="comment-tools"></div><div class="clear"></div><div id="comment-5020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5175"></span>

<div id="answer-container-5175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5175-score" class="post-score" title="current number of votes">0</div><span id="post-5175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As indicated in Jaap's <a href="http://ask.wireshark.org/questions/5166/registering-variables-in-a-dissector-code?page=1#5174" title="dissector variables answer">answer</a> to your other question, you only need one <code>static int hf_hb_cl_lvs</code>, not an entire array. If you want to track them all separately in your dissection function, then you would need to declare the array at the top of the function, not as <code>static</code> to your dissector (as this indicates the information is shared across all packets of your protocol). To put that into code, it might resemble the following:</p><pre><code>static int hf_hb_cl_lvs = -1;

...

static hf_register_info hf[] = 
{
    ...
    {&amp;hf_hb_cl_lvs, {&quot;hb_cl_lvs&quot;, &quot;foo.lvs&quot;, FT_UINT32, BASE_HEX, NULL, 0x0, &quot;LVS&quot;, HFILL}}
    ...
}

...

static void dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    int i = 0;
    gint offset = 0;
    guint32 LVS[32];

    ...

    for(i=0; i&lt;32; i++)
    {
        LVS[i] = tvb_get_ntohl(tvb, offset);
        if(LVS[i] != 0)
        {
            proto_tree_add_item(tree, hf_hb_cl_lvs, tvb, offset, 4, 0);
        }
        offset += 4;
    }

    ...

}</code></pre><p>Obviously you'd need to change this (names, data types, strings, etc.) to make it logically fit your data, but this represents a starting point for similar tasks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '11, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5175" class="comments-container"></div><div id="comment-tools-5175" class="comment-tools"></div><div class="clear"></div><div id="comment-5175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

