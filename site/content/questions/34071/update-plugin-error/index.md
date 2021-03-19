+++
type = "question"
title = "Update plugin error"
description = '''0 I have a plugin and I need to update it, I have done it to some extent but getting some errors. code =&amp;gt; https://github.com/amanpreet05/plugins/blob/master/packet-minet.c please help me how do I solve these errors error C2220: warning treated as error - no &#x27;object&#x27; file generated warning C4013: ...'''
date = "2014-06-23T06:00:00Z"
lastmod = "2014-06-23T09:43:00Z"
weight = 34071
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/34071" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Update plugin error](/questions/34071/update-plugin-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34071-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>0 I have a plugin and I need to update it, I have done it to some extent but getting some errors.</p><p>code =&gt; <a href="https://github.com/amanpreet05/plugins/blob/master/packet-minet.c">https://github.com/amanpreet05/plugins/blob/master/packet-minet.c</a></p><p>please help me how do I solve these errors</p><p>error C2220: warning treated as error - no 'object' file generated warning C4013: 'decode_boolean_bitfield' undefined; assuming extern returning int warning C4113: 'void (cdecl )(tvbuff_t ,packet_info ,proto_tree )' differs in parameter lists from 'new_dissector_t' warning C4133: 'function' : incompatible types - from 'void (cdecl )(tvbuff_t ,packet_info ,proto_tree )' to 'new_dissector_t'</p></div><div id="question-tags" class="tags-container tags">plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/a9a254ac482208f766093c0f9c144364?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aman&#39;s gravatar image" /><p>aman<br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aman has no accepted answers">0%</span></p></div></div><div id="comments-container-34071" class="comments-container"><span id="34074"></span><div id="comment-34074" class="comment"><div id="post-34074-score" class="comment-score"></div><div class="comment-text"><p>@kurt @grahamb please reply for this..</p></div><div id="comment-34074-info" class="comment-info"><span class="comment-age">(23 Jun '14, 06:20)</span> aman</div></div><span id="34076"></span><div id="comment-34076" class="comment"><div id="post-34076-score" class="comment-score"></div><div class="comment-text"><p>decode_boolean_bitfield has be depricated and removed. You will have to rewrite the code to use a different API. Like proto_tree_add_item() and define hf variables with the apropriate bitmask. Glancing at the dissector code it should probably be totaly rewritten to use proto_tree_add_item() and value_strings.</p></div><div id="comment-34076-info" class="comment-info"><span class="comment-age">(23 Jun '14, 06:51)</span> Anders ♦</div></div><span id="34077"></span><div id="comment-34077" class="comment"><div id="post-34077-score" class="comment-score"></div><div class="comment-text"><p>if I replace decode_boolean_bitfield() with proto_tree_add_item(), I need to change parameters as well or add a parameter to it?</p></div><div id="comment-34077-info" class="comment-info"><span class="comment-age">(23 Jun '14, 07:00)</span> aman</div></div></div><div id="comment-tools-34071" class="comment-tools"></div><div class="clear"></div><div id="comment-34071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34080"></span>

<div id="answer-container-34080" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34080-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>                    proto_tree_add_text(tree, tvb, tempOffset, 1, &quot;%s&quot;,                     decode_boolean_bitfield(tempByte, 0x80, 8,                              &quot;Overall Result: Ignored&quot;, &quot;Overall Result: Digits dialed on analog line</code></pre><p>Replace by:</p><p><code>proto_tree_add_item(tree, hf_your_new_hf, tvb, tempOffset, 1, ENC_BIG_ENDIAN);</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-34080" class="comments-container"></div><div id="comment-tools-34080" class="comment-tools"></div><div class="clear"></div><div id="comment-34080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34083"></span>

<div id="answer-container-34083" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34083-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Those questions were already answered in <a href="http://ask.wireshark.org/questions/33735/update-plugin-to-latest-wireshark-version">http://ask.wireshark.org/questions/33735/update-plugin-to-latest-wireshark-version</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-34083" class="comments-container"><span id="34084"></span><div id="comment-34084" class="comment"><div id="post-34084-score" class="comment-score"></div><div class="comment-text"><p>@pascal: they asked me for the git code so I updated it. Maybe this may help diagnose the exact error I am making.</p></div><div id="comment-34084-info" class="comment-info"><span class="comment-age">(23 Jun '14, 10:14)</span> aman</div></div><span id="34087"></span><div id="comment-34087" class="comment"><div id="post-34087-score" class="comment-score"></div><div class="comment-text"><p>If you read the thread again, you will see that Guy and myself already told you how to fix those two errors. Did you actually read our answers and tried to do the suggested changes? Of course we could fo the changes for you but it will not help you progress. Moreover we already provided you some info but you restart a new thread with the same for initial question without taking into account the answers already done. IMHO this is not nice for the people who spent time answering you (Guy did a far better job than myself).</p></div><div id="comment-34087-info" class="comment-info"><span class="comment-age">(23 Jun '14, 10:56)</span> Pascal Quantin</div></div><span id="34088"></span><div id="comment-34088" class="comment"><div id="post-34088-score" class="comment-score"></div><div class="comment-text"><p>@pascal: ya I appreciate the fact and I did read your comments, and you and Guy helped me a lot, and it did solve the thing but now I started this thread because I got the last comment to show the code on git. I thought maybe it could help more..</p></div><div id="comment-34088-info" class="comment-info"><span class="comment-age">(23 Jun '14, 11:04)</span> aman</div></div><span id="34092"></span><div id="comment-34092" class="comment"><div id="post-34092-score" class="comment-score"></div><div class="comment-text"><p>You will find here <a href="https://dl.dropboxusercontent.com/u/4857000/packet-minet.c">https://dl.dropboxusercontent.com/u/4857000/packet-minet.c</a> a version of packet-mimet.c that I quickly modified so as to have it compile. You will see that it is ugly as I did not take the time to replace the 59 calls to decode_boolean_bitfield() by a call to proto_add_item, but instead added back the code for the function as I suggested you in your previous thread (but it seems like you missed this comment). You can take it as an example to modify the other dissectors.</p><p>If you feel courageous enough, it would be a good thing to follow the advices done by Guy / Anders and remove all those calls to proto_tree_add_text as those items are not filterable.</p></div><div id="comment-34092-info" class="comment-info"><span class="comment-age">(23 Jun '14, 11:53)</span> Pascal Quantin</div></div><span id="34093"></span><div id="comment-34093" class="comment"><div id="post-34093-score" class="comment-score"></div><div class="comment-text"><p>Thanks @pascal for your help..</p></div><div id="comment-34093-info" class="comment-info"><span class="comment-age">(23 Jun '14, 12:30)</span> aman</div></div></div><div id="comment-tools-34083" class="comment-tools"></div><div class="clear"></div><div id="comment-34083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

