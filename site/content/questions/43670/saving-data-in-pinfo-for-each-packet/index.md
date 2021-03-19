+++
type = "question"
title = "saving data in pinfo for each packet"
description = '''Hi all, I am working on a dissector and have to save data after first iteration either a tvb or a buffer.I am trying to save it using add_new_data_source.My code looks something like this  guint8 *decrypted_buffer; &amp;lt;---do something with the buffer and fill it --&amp;gt; tvbuff_t *decrypt_tvb = tvb_ne...'''
date = "2015-06-29T09:20:00Z"
lastmod = "2015-06-30T03:30:00Z"
weight = 43670
keywords = [ "tvbuff_t", "pinfo" ]
aliases = [ "/questions/43670" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [saving data in pinfo for each packet](/questions/43670/saving-data-in-pinfo-for-each-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43670-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am working on a dissector and have to save data after first iteration either a tvb or a buffer.I am trying to save it using add_new_data_source.My code looks something like this</p><pre><code>guint8 *decrypted_buffer;
&lt;---do something with the buffer and fill it --&gt;
tvbuff_t *decrypt_tvb = tvb_new_child_real_data(tvb,decrypted_buffer,sizeof(decrypted_buffer),sizeof(decrypted_buffer));
add_new_data_source(pinfo,decrypted_tvb,&quot;Decrypted Data&quot;);</code></pre><p>I can see the new buffer in the ui beside the frame.But <strong>my aim is to save the buffer(or tvb) for the next iteration</strong>,so that I dont have to dissect the packet again instead just pass the stored buffer on to the dissector.Please suggest a way to store the buffer(or tvb) for the next iterations.</p><p>Thanks<br />
Koundinya.</p></div><div id="question-tags" class="tags-container tags">tvbuff_t pinfo</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '15, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-43670" class="comments-container"></div><div id="comment-tools-43670" class="comment-tools"></div><div class="clear"></div><div id="comment-43670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43714"></span>

<div id="answer-container-43714" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43714-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the p_add_proto_data/p_get_proto_data API described in doc/README.dissector chapter 2.5.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43714" class="comments-container"><span id="43719"></span><div id="comment-43719" class="comment"><div id="post-43719-score" class="comment-score"></div><div class="comment-text"><p>Saving the buffer might be a bad idea for large capture files as you will use huge amount of memory...</p></div><div id="comment-43719-info" class="comment-info"><span class="comment-age">(30 Jun '15, 03:46)</span> Anders ♦</div></div><span id="43729"></span><div id="comment-43729" class="comment"><div id="post-43729-score" class="comment-score"></div><div class="comment-text"><p>ah yes! I do agree with you on that so I will have to come up with a way to save small value that should not change even after any number of iterations .I did read the README.dissector file but unfortunately i still cant completely understand how conversation and p_add_proto_data are related!Anyways thank you guys for all the help!</p><p>Best Regards, Koundinya</p></div><div id="comment-43729-info" class="comment-info"><span class="comment-age">(30 Jun '15, 05:54)</span> koundi</div></div><span id="59285"></span><div id="comment-59285" class="comment"><div id="post-59285-score" class="comment-score"></div><div class="comment-text"><p>@anders @Pascal Quantin</p><p>Could you please give me an example of the implementation of p_add_proto_data/p_get_proto_data? I have been trying to apply it. but have been totally unsuccessful! Do you know if there is any wireshirk plugin where These has been used? Thanks</p></div><div id="comment-59285-info" class="comment-info"><span class="comment-age">(09 Feb '17, 07:05)</span> xaheen</div></div><span id="59288"></span><div id="comment-59288" class="comment"><div id="post-59288-score" class="comment-score"></div><div class="comment-text"><p>There are many, simply search for those functions in the dissectors, packet-xxx.c files (in epan/dissectors).</p></div><div id="comment-59288-info" class="comment-info"><span class="comment-age">(09 Feb '17, 07:32)</span> grahamb ♦</div></div><span id="59318"></span><div id="comment-59318" class="comment"><div id="post-59318-score" class="comment-score"></div><div class="comment-text"><blockquote><p>so I will have to come up with a way to save small value that should not change even after any number of iterations</p></blockquote><p>You mean like the decryption key used to decrypt the data? (I'm assuming each packet requires a separate key; if the entire session uses one key, it'd be best to save one copy attached to a "conversation" of some sort.)</p></div><div id="comment-59318-info" class="comment-info"><span class="comment-age">(09 Feb '17, 23:02)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-43714" class="comment-tools"></div><div class="clear"></div><div id="comment-43714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

