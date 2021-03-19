+++
type = "question"
title = "Disable packet count in tshark"
description = '''Topic says it..how do I disable the annoying packet count in tshark? Thank you.'''
date = "2014-05-07T04:44:00Z"
lastmod = "2014-05-14T04:40:00Z"
weight = 32586
keywords = [ "tshark" ]
aliases = [ "/questions/32586" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Disable packet count in tshark](/questions/32586/disable-packet-count-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32586-score" class="post-score" title="current number of votes">0</div><span id="post-32586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Topic says it..how do I disable the annoying packet count in tshark? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/feeceb13b3a434a147fa2c173ad18db8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngelXX&#39;s gravatar image" /><p><span>DigiAngelXX</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngelXX has no accepted answers">0%</span></p></div></div><div id="comments-container-32586" class="comments-container"></div><div id="comment-tools-32586" class="comment-tools"></div><div class="clear"></div><div id="comment-32586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32589"></span>

<div id="answer-container-32589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32589-score" class="post-score" title="current number of votes">1</div><span id="post-32589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure which version supports it but there is: tshark -h</p><p>:</p><p>-q be more quiet on stdout (e.g. when using statistics)</p><p>-Q only log true errors to stderr (quieter than -q)</p><p>:</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32589" class="comments-container"><span id="32592"></span><div id="comment-32592" class="comment"><div id="post-32592-score" class="comment-score"></div><div class="comment-text"><p>Yea I tried both of those...no luck but thanks.</p></div><div id="comment-32592-info" class="comment-info"><span class="comment-age">(07 May '14, 05:27)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div></div><div id="comment-tools-32589" class="comment-tools"></div><div class="clear"></div><div id="comment-32589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32598"></span>

<div id="answer-container-32598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32598-score" class="post-score" title="current number of votes">1</div><span id="post-32598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to <a href="http://ask.wireshark.org/questions/31564/tshark-output-refining">this</a> question, which was also asked in a similar question <a href="http://ask.wireshark.org/questions/32552/tshark-suppress-random-line-numbers">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-32598" class="comments-container"><span id="32625"></span><div id="comment-32625" class="comment"><div id="post-32625-score" class="comment-score"></div><div class="comment-text"><p>That explains it..thank you.</p></div><div id="comment-32625-info" class="comment-info"><span class="comment-age">(07 May '14, 16:53)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div><span id="32663"></span><div id="comment-32663" class="comment"><div id="post-32663-score" class="comment-score"></div><div class="comment-text"><p>So this....sorta worked. Looked at the r51227 and recompiled after making the changes to tshark.c. Now EVERY packet gets the packet count...which I guess is better then getting them sporadically.</p></div><div id="comment-32663-info" class="comment-info"><span class="comment-age">(09 May '14, 06:18)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div><span id="32665"></span><div id="comment-32665" class="comment"><div id="post-32665-score" class="comment-score"></div><div class="comment-text"><p>How are you running <code>tshark</code>? Can you post your <code>tshark</code> command-line?</p></div><div id="comment-32665-info" class="comment-info"><span class="comment-age">(09 May '14, 08:17)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="32697"></span><div id="comment-32697" class="comment"><div id="post-32697-score" class="comment-score"></div><div class="comment-text"><p>sudo tshark -t ad -n -i eth1 ip and host 192.168.1.1</p><p>This gets me a packet count on every line.</p></div><div id="comment-32697-info" class="comment-info"><span class="comment-age">(09 May '14, 17:10)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div><span id="32699"></span><div id="comment-32699" class="comment"><div id="post-32699-score" class="comment-score"></div><div class="comment-text"><p>You can control what is displayed via <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a>'s <code>-T fields</code> options or through the <code>-o gui.column.format</code> option. Run <code>tshark -G column-formats</code> for the various options.</p></div><div id="comment-32699-info" class="comment-info"><span class="comment-age">(09 May '14, 17:48)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="32792"></span><div id="comment-32792" class="comment not_top_scorer"><div id="post-32792-score" class="comment-score"></div><div class="comment-text"><p>Thanks...I guess that's my only option.</p></div><div id="comment-32792-info" class="comment-info"><span class="comment-age">(14 May '14, 04:40)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div></div><div id="comment-tools-32598" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

