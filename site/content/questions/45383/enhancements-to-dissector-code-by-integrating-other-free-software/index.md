+++
type = "question"
title = "Enhancements to dissector code by integrating other free software"
description = '''SO here is what I did, I used the source code of another free software under(GPL license) in my wireshark development version and made some enhancements that were not there in wireshark. Now I want to contribute it to the source. Is this setting fine? Or DO I have to rewrite all the code that I used...'''
date = "2015-08-26T23:51:00Z"
lastmod = "2015-08-31T11:48:00Z"
weight = 45383
keywords = [ "contributing", "source", "wireshark" ]
aliases = [ "/questions/45383" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Enhancements to dissector code by integrating other free software](/questions/45383/enhancements-to-dissector-code-by-integrating-other-free-software)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45383-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>SO here is what I did, I used the source code of another free software under(GPL license) in my wireshark development version and made some enhancements that were not there in wireshark. Now I want to contribute it to the source. Is this setting fine? Or DO I have to rewrite all the code that I used from the other software? Any insights? Thanks a lot! -Koundi</p></div><div id="question-tags" class="tags-container tags">contributing source wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '15, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div></div><div id="comments-container-45383" class="comments-container"><span id="45395"></span><div id="comment-45395" class="comment"><div id="post-45395-score" class="comment-score"></div><div class="comment-text"><p>GPL, as in GPL2, GPL2+, or GPL3? Unfortunately it does matter. See this <a href="https://www.gnu.org/licenses/gpl-faq.html#v2v3Compatibility">answer on compatibility</a>.</p></div><div id="comment-45395-info" class="comment-info"><span class="comment-age">(27 Aug '15, 04:09)</span> Jaap ♦</div></div><span id="45543"></span><div id="comment-45543" class="comment"><div id="post-45543-score" class="comment-score"></div><div class="comment-text"><p>@Jaap I dont think that is a problem looks like both are under GPL version 2 license!From what I read wireshark is under GPL 2 license right?</p></div><div id="comment-45543-info" class="comment-info"><span class="comment-age">(31 Aug '15, 00:17)</span> koundi</div></div></div><div id="comment-tools-45383" class="comment-tools"></div><div class="clear"></div><div id="comment-45383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45384"></span>

<div id="answer-container-45384" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45384-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know that is perfectly fine. I think it only may be a problem if the licenses differ.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-45384" class="comments-container"><span id="45386"></span><div id="comment-45386" class="comment"><div id="post-45386-score" class="comment-score"></div><div class="comment-text"><p>Thanks Anders for the prompt response. Both the softwares(wireshark and the other software) are under general public license(GPL).Are there are any more pitfalls that I need to be careful about ? -koundi</p></div><div id="comment-45386-info" class="comment-info"><span class="comment-age">(27 Aug '15, 01:12)</span> koundi</div></div><span id="45389"></span><div id="comment-45389" class="comment"><div id="post-45389-score" class="comment-score"></div><div class="comment-text"><p>Seems as though the licences are OK, now you need to think about all the platforms Wireshark runs on, e.g. Linux, OSX, Windows, Solaris and a few others.</p><p>Does your other software run on the above platforms?</p></div><div id="comment-45389-info" class="comment-info"><span class="comment-age">(27 Aug '15, 01:53)</span> grahamb ♦</div></div><span id="45393"></span><div id="comment-45393" class="comment"><div id="post-45393-score" class="comment-score"></div><div class="comment-text"><p>I have checked on windows and Linux. But given that we have access to the source code, it wont be a problem as we can always include os specific headers. Right ? Thanks -Koundi</p></div><div id="comment-45393-info" class="comment-info"><span class="comment-age">(27 Aug '15, 04:02)</span> koundi</div></div><span id="45398"></span><div id="comment-45398" class="comment"><div id="post-45398-score" class="comment-score"></div><div class="comment-text"><p>If you are linking to other libraries it might need discussion, if you are copying code it's more of a licencing question, I think. But you'd have to be more specific. One way is to upload your code yo gerrit and have it reviewed.</p></div><div id="comment-45398-info" class="comment-info"><span class="comment-age">(27 Aug '15, 05:03)</span> Anders ♦</div></div><span id="45473"></span><div id="comment-45473" class="comment"><div id="post-45473-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I used the source code of another free software under(GPL license) in my wireshark development</p></blockquote><p>what is that <strong>other</strong> software?</p></div><div id="comment-45473-info" class="comment-info"><span class="comment-age">(28 Aug '15, 08:21)</span> Kurt Knochner ♦</div></div><span id="45542"></span><div id="comment-45542" class="comment not_top_scorer"><div id="post-45542-score" class="comment-score"></div><div class="comment-text"><p>@kurt I have integrated this code into my development version (<a href="https://github.com/gteissier/srtp-decrypt).">https://github.com/gteissier/srtp-decrypt).</a> After making a bunch of changes adding some code of my own to create UI for keys, support multiple streams and handling some other issues. -koundi</p></div><div id="comment-45542-info" class="comment-info"><span class="comment-age">(31 Aug '15, 00:12)</span> koundi</div></div></div><div id="comment-tools-45384" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-45384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45551"></span>

<div id="answer-container-45551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45551-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Great! Please follow the steps at <a href="https://www.wireshark.org/develop.html">https://www.wireshark.org/develop.html</a> to submit your patch. Make sure you include the Copyright and author messages of the project(s) your code is using.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '15, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/f1397f7833ee927f0c26a9fcb92fff11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmayer&#39;s gravatar image" /><p>jmayer<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmayer has no accepted answers">0%</span></p></div></div><div id="comments-container-45551" class="comments-container"></div><div id="comment-tools-45551" class="comment-tools"></div><div class="clear"></div><div id="comment-45551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

