+++
type = "question"
title = "diameter protocol wireshark source code"
description = '''Hello, I want to ask some questions about diameter protocol :  I have donwloaded the source code of wireshark and I go into the folder wireshark-2.0.2/epan to see the file diam_dict.l   I want to know why wireshark has used lex and yacc (or flex and bison) but not other xml parser (like libxml2) to ...'''
date = "2016-04-21T07:40:00Z"
lastmod = "2016-04-22T00:25:00Z"
weight = 51839
keywords = [ "source-code", "diameter", "protocol" ]
aliases = [ "/questions/51839" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [diameter protocol wireshark source code](/questions/51839/diameter-protocol-wireshark-source-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51839-score" class="post-score" title="current number of votes">0</div><span id="post-51839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I want to ask some questions about diameter protocol :<br />
</p><p>I have donwloaded the source code of wireshark and I go into the folder wireshark-2.0.2/epan to see the file diam_dict.l<br />
</p><ol><li>I want to know why wireshark has used lex and yacc (or flex and bison) but not other xml parser (like libxml2) to parse the diameter protocol dictionary (wireshark-2.0.2/diameter/dictionary.xml)</li><li>And I want to know why wireshark has put the lex file and the yacc file together, so that there is just one file (in other words wireshark-2.0.2/epan/diam_dict.l). Normally, we have lex files (like diam_dict.l ==&gt; lex.yy.c) and yacc files (diam_dict.y ==&gt; y.tab.h &amp; y.tab.c)</li><li>In fact, I am now doing a project to try to replace the role of lex and yacc (the role of xml parser (in particulary I only want to paser the file wireshark-2.0.2/diameter/dictionary.xml)), to replace it with another xml parser (libxml2), do you have any advice ? (Now I am studying the functions of the file wireshark-2.0.2/epan/diam_dict.l, so that I can write by myself another file using the libxml2 library to do exactly the same thing)</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source-code" rel="tag" title="see questions tagged &#39;source-code&#39;">source-code</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '16, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/78d9dce3b7a6f4e7de233c01445171c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bohao&#39;s gravatar image" /><p><span>bohao</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bohao has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-51839" class="comments-container"></div><div id="comment-tools-51839" class="comment-tools"></div><div class="clear"></div><div id="comment-51839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51847"></span>

<div id="answer-container-51847" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51847-score" class="post-score" title="current number of votes">1</div><span id="post-51847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bohao has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to know why wireshark has used lex and yacc (or flex and bison)</p></blockquote><p>No, just Flex (and it's required Flex for a while now; the version in the trunk not only requires Flex, it requires a version new enough to support reentrant parsers). There's no YACC/Bison/Berkeley YACC parser there.</p><blockquote><p>And I want to know why wireshark has put the lex file and the yacc file together</p></blockquote><p>They're not together - there <em>is</em> no YACC file.</p><blockquote><p>to replace it with another xml parser (libxml2), do you have any advice ?</p></blockquote><p>In addition to making sure that an XML parser will actually <em>accept</em> the dictionary, also make sure that libxml2 can be made to work on <em>all</em> our supported platforms, including Windows, and that you don't depend on features of libxml2 only available in versions of libxml2 not present in commonly-used versions of {Linux distributions, *BSDs, OS X, other commercial UN*Xes} that bundle libxml2 (it'd be best if Wireshark could build on those versions without the user having to install a newer version of libxml2).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '16, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51847" class="comments-container"><span id="51856"></span><div id="comment-51856" class="comment"><div id="post-51856-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for your answer, that really helped me a lot.</p><pre><code>  So you mean that wireshark has used flex (rather than other xml parsers) because that it is compatible on diffrent operating systems (if there is another reason for this, please tell me) ?

  And, in fact, I haven&#39;t decided which xml parser to use yet, libxml2 is just a tool that someone advised me to use. I want to just use a xml parser for language c because this is the language that I use the most frequetly. So if you know another better xml parser for language c you can tell me :)

  (at this moment I am studying the functions and the data structure of the file wireshark-2.0.2/epan/diam_dict.l, so that I can imitate the functions of this file by replacing the original paser (flex) by another xml parser. )</code></pre><p>Good day.</p></div><div id="comment-51856-info" class="comment-info"><span class="comment-age">(22 Apr '16, 00:02)</span> <span class="comment-user userinfo">bohao</span></div></div></div><div id="comment-tools-51847" class="comment-tools"></div><div class="clear"></div><div id="comment-51847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51844"></span>

<div id="answer-container-51844" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51844-score" class="post-score" title="current number of votes">1</div><span id="post-51844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think to know <em>why</em> we'd have to ask the original author who hasn't been working on Wireshark in some time. IOW I don't think it will be easy to find out. But, see the next paragraph.</p><p>For question (3) I'd suggest first checking if the the XML is actually syntactically correct. A while back I ran xmllint on it and cleaned up a lot of the errors but there were still a large number left--mostly things that, frankly, it didn't seem worth fixing. IOW a proper XML parser may not be happy with our (pseudo-?) XML. This may be part of the reason we don't use a proper XML parser.</p><p>Oh, actually the first commit of diam_dict.l indicates that we used to use libxml but that it was intentionally dropped:</p><pre><code>commit b0bd83c868af357fffc971157f4bae2b7060073d
Author: Luis Ontanon &lt;[email protected]&gt;
Date:   Mon Jul 16 05:41:58 2007 +0000

    Rewrite of the diameter dissector to use the dictionary for creating hfids, drop libxml dependency.</code></pre><p>A little more research suggests that the <a href="https://www.wireshark.org/lists/ethereal-dev/200406/msg00292.html">lack of a (fully supported or at least working) Windows version</a> may have been what killed our use of it off. (There are other messages on the mailing lists suggesting plenty of people being unhappy because the Diameter dissector didn't work on Windows.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '16, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-51844" class="comments-container"><span id="51857"></span><div id="comment-51857" class="comment"><div id="post-51857-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-51857-info" class="comment-info"><span class="comment-age">(22 Apr '16, 00:25)</span> <span class="comment-user userinfo">bohao</span></div></div></div><div id="comment-tools-51844" class="comment-tools"></div><div class="clear"></div><div id="comment-51844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

