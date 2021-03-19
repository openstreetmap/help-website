+++
type = "question"
title = "Why Wiresharks shows protocol UNKNOWN and WTAP_ENCAP=1 for all packets?"
description = ''''''
date = "2016-06-21T21:58:00Z"
lastmod = "2016-06-22T04:18:00Z"
weight = 53599
keywords = [ "unknown", "wtap_encap" ]
aliases = [ "/questions/53599" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why Wiresharks shows protocol UNKNOWN and WTAP\_ENCAP=1 for all packets?](/questions/53599/why-wiresharks-shows-protocol-unknown-and-wtap_encap1-for-all-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_SdAHciG.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">unknown wtap_encap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '16, 21:58</strong></p><img src="https://secure.gravatar.com/avatar/af78d88051bc8bb505421771768a1d6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Frater&#39;s gravatar image" /><p>Andrew Frater<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Frater has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '16, 22:23</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53599" class="comments-container"><span id="53600"></span><div id="comment-53600" class="comment"><div id="post-53600-score" class="comment-score"></div><div class="comment-text"><p>Each post should have a clear, specific question in the title field. Please rephrase the title as a proper question.</p></div><div id="comment-53600-info" class="comment-info"><span class="comment-age">(21 Jun '16, 23:07)</span> Jaap ♦</div></div><span id="53606"></span><div id="comment-53606" class="comment"><div id="post-53606-score" class="comment-score"></div><div class="comment-text"><p>Or, in another words, from what you've provided we can only guess what is your problem. E.g. my guess is that you have disabled the ethernet dissector, but as you have provided a screenshot instead of a capture file, and you show frame 1 in the lower two panes but other frames in the packet list pane, it is not more than a guess.</p></div><div id="comment-53606-info" class="comment-info"><span class="comment-age">(22 Jun '16, 04:25)</span> sindy</div></div></div><div id="comment-tools-53599" class="comment-tools"></div><div class="clear"></div><div id="comment-53599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53605"></span>

<div id="answer-container-53605" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53605-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have deactivated Ethernet dissector.</p><p>Go to Analyze -&gt; Enabled Protocols and ensure that Ethernet is checked (you might also need to check any other deactivated dissector you might need).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '16, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-53605" class="comments-container"><span id="53619"></span><div id="comment-53619" class="comment"><div id="post-53619-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Problem solved, I was unaware that asking a question was done wrong. This is the first time i have done this my bad to all those i seemed to upset? again though much thanks on my side.</p></div><div id="comment-53619-info" class="comment-info"><span class="comment-age">(22 Jun '16, 15:20)</span> Andrew Frater</div></div><span id="53622"></span><div id="comment-53622" class="comment"><div id="post-53622-score" class="comment-score"></div><div class="comment-text"><p>The idea of the site is to build a Q&amp;A knowledge base. Given the total number of questions, it can only be useful if not only the Answers are useful but also the Questions can be searched through on keywords and tags, so that other people coming with the same problem can find a similar Question already answered (and that Google search takes them to the right Question).</p><p>For the same purpose, if an Answer was useful to you, please mark it as such by clicking the checkmark icon next to it. Questions with useful Answers appear in different colour in the list so people coming with the same problem can immediately see whether the Answer was useful. No one else than you can do that - all the others may vote for the Answers but that doesn't make the Question change colour in the list.</p><p>So I've changed the title of your question to one I deem useful. I've also converted your last post from an Answer (which it was not because it did not answer your original Question) into a Comment to @Pascal Quantin's Answer. But no one else than you can mark Pascal's Answer as useful.</p></div><div id="comment-53622-info" class="comment-info"><span class="comment-age">(22 Jun '16, 22:38)</span> sindy</div></div><span id="53624"></span><div id="comment-53624" class="comment"><div id="post-53624-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p><p>Like @sindy said this is a Q&amp;A knowledge base, not a general user forum. Therefore certain constraints apply and format required.</p></div><div id="comment-53624-info" class="comment-info"><span class="comment-age">(23 Jun '16, 00:35)</span> Jaap ♦</div></div></div><div id="comment-tools-53605" class="comment-tools"></div><div class="clear"></div><div id="comment-53605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

