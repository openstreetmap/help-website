+++
type = "question"
title = "epan_dissect_t not being passed to stats_tree correctly"
description = '''I&#x27;ve written a protocol dissector plugin for a protocol that uses CORBA for some of its communication. This protocol can send objects that can have any number of member variables and each object has a 64bit id. I have a text file with an text name and ID mapping. I&#x27;m able to correctly identify the m...'''
date = "2013-09-11T16:44:00Z"
lastmod = "2013-09-17T09:35:00Z"
weight = 24595
keywords = [ "tap_listener", "dissector", "stats_tree", "plugin" ]
aliases = [ "/questions/24595" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [epan\_dissect\_t not being passed to stats\_tree correctly](/questions/24595/epan_dissect_t-not-being-passed-to-stats_tree-correctly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24595-score" class="post-score" title="current number of votes">0</div><span id="post-24595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written a protocol dissector plugin for a protocol that uses CORBA for some of its communication. This protocol can send objects that can have any number of member variables and each object has a 64bit id. I have a text file with an text name and ID mapping. I'm able to correctly identify the messages in wireshark during dissection.<br />
I'm trying to to do a stats_tree for this protocol to identify the different object types received. A tap listener has been written along with stats_tree code. When the stats_tree callback for the packet is called, the pinfo current_proto has "&lt;missing protocol="" name=""&gt;" for its value. The epan_dissect_t has a tvb with values that I don't recognize and doesn't look like the values from my protocol.<br />
</p><p>My dissector plugin code is loosely based off of packet-coseventcomm.c. I call tap_queue_packet right after decode_CosEventComm_PushConsumer_push in the function dissect_coseventcomm. The objects I'm interested in dissected get dissected in decode_CosEventComm_PushConsumer_push so I dissect them in there and after that function I call tap_queue_packet.</p><p>Does the stats_tree packet callback get called on the packet that gets queued by tap_queue_packet? Does the callback receive the tvb data starting with the same data that gets sent to the dissector? I'm having a hard time trying to figure out what I'm doing wrong.<br />
</p><p>I register the tap listener and the stats_tree plugins with the following code</p><pre><code>G_MODULE_EXPORT void plugin_register_tap_listener(void) {

    GString *error_string;
    error_string = register_tap_listener(&quot;TOMA&quot;, NULL, NULL, 0, toma_tap_packet_init,
        toma_tap_packet, NULL);

    if (error_string)
    {
        fprintf(stderr, &quot; %s\n&quot;,
            error_string-&gt;str);
        g_string_free(error_string, TRUE);
    }

    stats_tree_register_plugin(&quot;tomatcp&quot;,
        &quot;tomatcp&quot;, 
        st_str_toma,
        TL_REQUIRES_PROTO_TREE,/*  TL_REQUIRES_PROTO_TREE*/
        toma_stats_tree_packet,
        toma_stats_tree_init,
        NULL);

}</code></pre><p>Thanks for any help with this issue.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tap_listener" rel="tag" title="see questions tagged &#39;tap_listener&#39;">tap_listener</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-stats_tree" rel="tag" title="see questions tagged &#39;stats_tree&#39;">stats_tree</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '13, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-24595" class="comments-container"></div><div id="comment-tools-24595" class="comment-tools"></div><div class="clear"></div><div id="comment-24595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24854"></span>

<div id="answer-container-24854" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24854-score" class="post-score" title="current number of votes">0</div><span id="post-24854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After doing a lot of digging in the source and refreshing of my memory it seems like I was looking at data in the wrong data structure. Although, I didn't even need to do that.<br />
I ended up calling tap_queue_packet right after the necessary object gets dissected and just passing an ephemeral created data structure with the info I needed.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-24854" class="comments-container"></div><div id="comment-tools-24854" class="comment-tools"></div><div class="clear"></div><div id="comment-24854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

