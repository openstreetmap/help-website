+++
type = "question"
title = "Wireshark dissector with pcapng format file - access section/interface description fields"
description = '''I am writing a custom protocol wireshark dissector in C as a plugin. I have got the dissector working . I am not able to figure out if there is a way to access the information we fill in section header / interface description header from our dissector? There seem to be tvbuff and packet_info passed ...'''
date = "2016-12-14T10:17:00Z"
lastmod = "2016-12-14T14:13:00Z"
weight = 58090
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/58090" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark dissector with pcapng format file - access section/interface description fields](/questions/58090/wireshark-dissector-with-pcapng-format-file-access-sectioninterface-description-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58090-score" class="post-score" title="current number of votes">0</div><span id="post-58090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a custom protocol wireshark dissector in C as a plugin. I have got the dissector working . I am not able to figure out if there is a way to access the information we fill in section header / interface description header from our dissector? There seem to be tvbuff and packet_info passed , which don't have this information.</p><p>Is there a way to access these fields?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '16, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/dd9838ab086fed6c7c24a109d07abe8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rashmi_s&#39;s gravatar image" /><p><span>rashmi_s</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rashmi_s has no accepted answers">0%</span></p></div></div><div id="comments-container-58090" class="comments-container"><span id="58091"></span><div id="comment-58091" class="comment"><div id="post-58091-score" class="comment-score"></div><div class="comment-text"><p>Exactly what information are you looking for? Have you examined the pinfo structure passed into your dissector?</p></div><div id="comment-58091-info" class="comment-info"><span class="comment-age">(14 Dec '16, 10:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="58092"></span><div id="comment-58092" class="comment"><div id="post-58092-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>I want to access the options fields (comment , os , hw etc) and other options fields I filled in section header and interface description block. I did have a look into pinfo , it seems to contain the metadata from enhanced packet block. Please correct me if I am wrong , is there any field in pinfo which will give access to section header and interface description options?</p></div><div id="comment-58092-info" class="comment-info"><span class="comment-age">(14 Dec '16, 10:31)</span> <span class="comment-user userinfo">rashmi_s</span></div></div><span id="58103"></span><div id="comment-58103" class="comment"><div id="post-58103-score" class="comment-score"></div><div class="comment-text"><p>Is there any documentation explaining the pinfo structure in detail? I am not able to find section header or interface description options in pinfo.</p></div><div id="comment-58103-info" class="comment-info"><span class="comment-age">(14 Dec '16, 12:43)</span> <span class="comment-user userinfo">rashmi_s</span></div></div></div><div id="comment-tools-58090" class="comment-tools"></div><div class="clear"></div><div id="comment-58090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58108"></span>

<div id="answer-container-58108" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58108-score" class="post-score" title="current number of votes">0</div><span id="post-58108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rashmi_s has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to access these fields?</p></blockquote><p>There's no supported mechanism to get at options in a Section Header Block or an Interface Description Block.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-58108" class="comments-container"></div><div id="comment-tools-58108" class="comment-tools"></div><div class="clear"></div><div id="comment-58108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

