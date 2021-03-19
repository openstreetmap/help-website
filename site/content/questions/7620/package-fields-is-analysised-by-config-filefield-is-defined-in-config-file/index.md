+++
type = "question"
title = "package fields is analysised by config file.field is defined in config file."
description = '''hi!I need wireshark dissect captured packages by a config file. When wireshark started,the config file will be loaded to wireshark,and the captured package will be dissected by the fields name defined in xml file. Every displayed field is defined in xml files,so every field is configurable .Could yo...'''
date = "2011-11-24T19:38:00Z"
lastmod = "2011-11-25T11:44:00Z"
weight = 7620
keywords = [ "xml", "dynamic", "analysis", "plugins" ]
aliases = [ "/questions/7620" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [package fields is analysised by config file.field is defined in config file.](/questions/7620/package-fields-is-analysised-by-config-filefield-is-defined-in-config-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7620-score" class="post-score" title="current number of votes">0</div><span id="post-7620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi!I need wireshark dissect captured packages by a config file. When wireshark started,the config file will be loaded to wireshark,and the captured package will be dissected by the fields name defined in xml file. Every displayed field is defined in xml files,so every field is configurable .Could you help me? Give me an example.Thank you very much!!! chinese is :我想通过XML配置文件的方式来解析wireshark所抓到的数据包。也就是说，我把消息字段配置到XML文件中，在抓包的过程中根据XML配置字段动态地解析数据包，不知道是否可行？如果可以，你们那边可以给我一个示例吗？非常感谢各位大侠！</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '11, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/ec135cb49b14f80b53d5875012660369?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="liyunshi&#39;s gravatar image" /><p><span>liyunshi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="liyunshi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 21:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-7620" class="comments-container"></div><div id="comment-tools-7620" class="comment-tools"></div><div class="clear"></div><div id="comment-7620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7625"></span>

<div id="answer-container-7625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7625-score" class="post-score" title="current number of votes">1</div><span id="post-7625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, Yo can have a look at the Diameter dissector packet-diameter.c which does something similar with the AVP:s.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-7625" class="comments-container"></div><div id="comment-tools-7625" class="comment-tools"></div><div class="clear"></div><div id="comment-7625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7634"></span>

<div id="answer-container-7634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7634-score" class="post-score" title="current number of votes">1</div><span id="post-7634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not XML, but there's <a href="http://wsgd.free.fr/">the Wireshark Generic Dissector</a> plugin, which accepts descriptions of protocols in its own (again, not XML-based) language.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7634" class="comments-container"></div><div id="comment-tools-7634" class="comment-tools"></div><div class="clear"></div><div id="comment-7634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

