+++
type = "question"
title = "Regular Expressions for parsing with IP spam source"
description = '''Hello, I&#x27;m trying to see email address with regular expression from a specific source IP that is doing spam from the corporate office.  I m using EnCase Software for data analysis and I need to create a full listing email and IP destination. Is there a way to capture frame who contains Email Address...'''
date = "2013-05-02T01:06:00Z"
lastmod = "2013-05-02T08:59:00Z"
weight = 20893
keywords = [ "regex", "spam" ]
aliases = [ "/questions/20893" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Regular Expressions for parsing with IP spam source](/questions/20893/regular-expressions-for-parsing-with-ip-spam-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20893-score" class="post-score" title="current number of votes">0</div><span id="post-20893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to see email address with regular expression from a specific source IP that is doing spam from the corporate office.</p><p>I m using EnCase Software for data analysis and I need to create a full listing email and IP destination.</p><p>Is there a way to capture frame who contains Email Address and to see them in a column ?</p><p>I'm using tis command : ip.src==192.168.217.128/24 frame contains "mailto:" but I would like to use regex to catch the destination email target</p><p>I'm using those regex for the email but I do not know how to input them in Wireshark :</p><blockquote><p>\b[A-Z0-9._%+-]<span class="__cf_email__" data-cfemail="d6fd96">[email protected]</span>[A-Z0-9.-]+.[A-Z]{2,4}\b</p><p>[a-z#~.!#$%\^&amp;*()-]<span class="__cf_email__" data-cfemail="775c37">[email protected]</span>[a-z#-]+.(com)|(biz)|(de)|(edu)|(gov)|(info)|(mil)|(net)|(org)|(tv)|(uk)|(jp)</p><p>[a-z#~.!#$%\^&amp;*()-]<span class="__cf_email__" data-cfemail="94bfd4">[email protected]</span>[a-z#-]+.[a-z#_-.]+</p><p>[a-z0-9!#$%&amp;'+/=?^<em>{|}~-]+(?:.[a-z0-9!#$%&amp;'*+/=?^</em>{|}~-]+)@(?:a-z0-9?.)+a-z0-9?</p></blockquote><p>Is there anybody who could help me please ? thx</p><p><a href="http://imagebin.org/256053">http://imagebin.org/256053</a> <a href="http://imagebin.org/256054">http://imagebin.org/256054</a> <a href="http://imagebin.org/256056">http://imagebin.org/256056</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-spam" rel="tag" title="see questions tagged &#39;spam&#39;">spam</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '13, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/bdfdd2512550033727374895b30f9ce1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arnaud68fr&#39;s gravatar image" /><p><span>arnaud68fr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arnaud68fr has no accepted answers">0%</span></p></div></div><div id="comments-container-20893" class="comments-container"></div><div id="comment-tools-20893" class="comment-tools"></div><div class="clear"></div><div id="comment-20893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20901"></span>

<div id="answer-container-20901" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20901-score" class="post-score" title="current number of votes">1</div><span id="post-20901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your question is really off-topic on this site, as we are discussing <strong>Wireshark</strong> issues here and not Encase product configuration issues.</p><p>I'm sure you have a valid license and thus your are entitled to call the Encase support hotline regarding any product configuration issues.</p><blockquote><p><a href="http://www.guidancesoftware.com/customer-service.htm">http://www.guidancesoftware.com/customer-service.htm</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20901" class="comments-container"><span id="20902"></span><div id="comment-20902" class="comment"><div id="post-20902-score" class="comment-score"></div><div class="comment-text"><p>Why creating a forum if I m not allow to post question ?? This is not a encase problem (cause I have some answer with encase) I need to give answer in real time for my company ? This is a law problem, I have to give information about a user who is doing sex spam.</p><p>I think that my question is not out of topic !! but reality for french law's in enterprise.</p></div><div id="comment-20902-info" class="comment-info"><span class="comment-age">(02 May '13, 04:24)</span> <span class="comment-user userinfo">arnaud68fr</span></div></div><span id="20904"></span><div id="comment-20904" class="comment"><div id="post-20904-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Why creating a forum if I m not allow to post question ??</p></blockquote><p>well, you are allowed to post a question. In fact I'm currently answering your question.</p><blockquote><p>I'm using those regex for the email but I do not know how to input them in Wireshark :</p></blockquote><p>As you are asking for a Wireshark regexp, here we go.</p><p>Pleas use this Display filter.</p><blockquote><p><code>ip.addr eq x.x.x.x and frame matches "[A-Za-z0-9+-_%][email protected]([A-Za-z0-9-]+\.)+[A-Za-z0-9-]+"</code><br />
</p></blockquote><p>The regexp may not be perfect, but it will match everything that looks like an e-mail address<br />
</p><blockquote><p><span class="__cf_email__" data-cfemail="e1929593888f86a1929593888f86cf929593888f86cf929593888f86cfcfcfcf">[email protected]</span></p></blockquote><p>As you don't know how the domain looks like (could be <code>[email protected]</code>) I did not restrict the length of the pattern, which might also then match to something that is not a valid domain/host name.</p></div><div id="comment-20904-info" class="comment-info"><span class="comment-age">(02 May '13, 05:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20901" class="comment-tools"></div><div class="clear"></div><div id="comment-20901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20903"></span>

<div id="answer-container-20903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20903-score" class="post-score" title="current number of votes">1</div><span id="post-20903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to match packets that contain the whole string, you can use:</p><pre><code>frame matches &quot;[A-Z0-9._%+-][email protected][A-Z0-9.-]+.[A-Z]{2,4}&quot;</code></pre><p>However, the whole string can be split accross packets which the filter does not catch. Over what protocols do you expect the email addresses to be sent? Http? If so, make sure you have reassembly enabled and then use the filter:</p><pre><code>http matches &quot;[A-Z0-9._%+-][email protected][A-Z0-9.-]+.[A-Z]{2,4}&quot;</code></pre><p>But other tools might be a better choice in your case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-20903" class="comments-container"><span id="20909"></span><div id="comment-20909" class="comment"><div id="post-20909-score" class="comment-score"></div><div class="comment-text"><p>Dear Kurt and SYN-bit,</p><p>Thanks a lot for your help, it's working fine.</p><p>Best regards,</p><p>Arnaud</p></div><div id="comment-20909-info" class="comment-info"><span class="comment-age">(02 May '13, 08:59)</span> <span class="comment-user userinfo">arnaud68fr</span></div></div></div><div id="comment-tools-20903" class="comment-tools"></div><div class="clear"></div><div id="comment-20903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

