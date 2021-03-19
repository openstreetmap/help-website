+++
type = "question"
title = "How to replace and free data of Tvb"
description = '''Hi all,  I&#x27;m changing source code of packet-data.c of wireshark for some specific purposes. In my scenario, I have to replace all data of a tvb with new data so that I use this one: tvb = tvb_new_real_data(real_data_sonnh,bytes+nSccp_length+6,bytes+nSccp_length+6);  where real_data_sonnh is a pointe...'''
date = "2014-12-07T18:23:00Z"
lastmod = "2014-12-09T00:10:00Z"
weight = 38422
keywords = [ "tvb_new_real_data", "free" ]
aliases = [ "/questions/38422" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to replace and free data of Tvb](/questions/38422/how-to-replace-and-free-data-of-tvb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38422-score" class="post-score" title="current number of votes">0</div><span id="post-38422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm changing source code of <strong>packet-data.c</strong> of wireshark for some specific purposes. In my scenario, I have to replace all data of a tvb with new data so that I use this one:</p><pre><code>tvb = tvb_new_real_data(real_data_sonnh,bytes+nSccp_length+6,bytes+nSccp_length+6);</code></pre><p>where real_data_sonnh is a pointer to my new data. But I realize that by doing this, the old data of tvb still exists and cannot be free when wireshark is running. My question is:</p><ul><li>How can I replace the old data of tvb and make sure that this data is free when I use tvb_new_real_data for the new data?</li></ul><p>Please help if you have any experience? Thank you so much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tvb_new_real_data" rel="tag" title="see questions tagged &#39;tvb_new_real_data&#39;">tvb_new_real_data</span> <span class="post-tag tag-link-free" rel="tag" title="see questions tagged &#39;free&#39;">free</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '14, 18:23</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '14, 01:16</strong> </span></p></div></div><div id="comments-container-38422" class="comments-container"></div><div id="comment-tools-38422" class="comment-tools"></div><div class="clear"></div><div id="comment-38422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38424"></span>

<div id="answer-container-38424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38424-score" class="post-score" title="current number of votes">0</div><span id="post-38424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Let me ask you another question: Do you see a dissector free its passed in TVB? The answer is: no. Consider the TVB that's handed to the dissector as an object owned by the dissection engine, which will handle its deallocation when it goes out of scope.</p><p>What you should worry about is freeing the new TVB you create. That is a TVB you own and the dissection engine doesn't know about.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '14, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-38424" class="comments-container"><span id="38425"></span><div id="comment-38425" class="comment"><div id="post-38425-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap, I don't want to create any TVB new. I just need to change some values and apply this change to the current TVB before it is going through the dissector. I'm not familiar with tvb allocation and deallocation, so that I tried to use</p><blockquote><p>tvb = tvb_new_real_data(real_data_sonnh,bytes+nSccp_length+6,bytes+nSccp_length+6);</p></blockquote><p>where tvb is the current tvb, real_data_sonnh is the pointer to the new data in order to make tvb has the new values. My question is: - If I use this code, do I need to free anything ? - is it better to create a new tvb with the new data and put it to the dissector instead of replacing the current tvb with a new data?</p><p>Thanks for your help.</p></div><div id="comment-38425-info" class="comment-info"><span class="comment-age">(08 Dec '14, 01:22)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="38428"></span><div id="comment-38428" class="comment"><div id="post-38428-score" class="comment-score"></div><div class="comment-text"><ul><li>You probably shouldn't modyfy packet-data.c but rather the caller of that dissector.</li><li>A tvb is supposed to contain the content of the packet and there shouldn't be any need to modify it unless the content is "packed" in some way and needs some sort of "deflating/decryption" to show the un packed content.</li><li>If you add new real data to a tvb you can set the function to be used when the dissection engine decides to free the tvb with tvb_set_free_cb() see sigcomp-udvm.c for example.</li></ul></div><div id="comment-38428-info" class="comment-info"><span class="comment-age">(08 Dec '14, 04:11)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="38461"></span><div id="comment-38461" class="comment"><div id="post-38461-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders, you are right. I don't want to modify packet-data.c and the data of tvb but I must do this because the content is packed and it must be decoded before going through the dissector.</p><p>About using <strong>tvb_set_free_cb()</strong>, I see it is used for <strong>tvb_new_child_real_data</strong> in most cases but not sure it could be used for <strong>tvb_new_real_data</strong></p><pre><code>tvb = tvb_new_real_data(real_data_sonnh,bytes+nSccp_length+6,bytes+nSccp_length+6);</code></pre><p>Also, if I use tvb_new_real_data to replace some old values of tvb, do I need to free anything? or just set a function tvb_set_free_cb() as below:</p><pre><code>tvb = tvb_new_real_data(real_data_sonnh,bytes+nSccp_length+6,bytes+nSccp_length+6); tvb_set_free_cb( tvb , g_free );</code></pre><p>My code structure is:</p><pre><code> dissect_data(tvbuff_t *tvb, packet_info *pinfo _U_ , proto_tree *tree)
{
  ...
  tvb = tvb_new_real_data(real_data_sonnh,bytes+nSccp_length+6,bytes+nSccp_length+6);
  ...
  if (new_pane) {
    guint8 *real_data = (guint8 *)tvb_memdup(tvb, 0, bytes);
    data_tvb = tvb_new_child_real_data(tvb,real_data,bytes,bytes);
    add_new_data_source(pinfo, data_tvb, &quot;Not dissected data bytes&quot;);
  } else {
            data_tvb = tvb;
           }
  dissect_data_sonnh(data_tvb,pinfo,tree );
  ...
}</code></pre><p>Do I need to free the old tvb ?</p></div><div id="comment-38461-info" class="comment-info"><span class="comment-age">(09 Dec '14, 00:10)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-38424" class="comment-tools"></div><div class="clear"></div><div id="comment-38424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

