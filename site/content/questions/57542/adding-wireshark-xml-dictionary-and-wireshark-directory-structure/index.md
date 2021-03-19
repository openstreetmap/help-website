+++
type = "question"
title = "Adding Wireshark xml dictionary and Wireshark directory structure"
description = '''Hi, I have prepared the .xml file for diameter dictionary for Vendor specific AVP. It works on Windows-based Wireshark installation however under Red Hat I find the directory for adding the dictionary missing. How I can solve the issue? Directory /.wireshark : /# ls -a . .. cfilters colorfilters dic...'''
date = "2016-11-22T03:09:00Z"
lastmod = "2016-11-22T04:23:00Z"
weight = 57542
keywords = [ "diameter", "redhat", "dictionary" ]
aliases = [ "/questions/57542" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding Wireshark xml dictionary and Wireshark directory structure](/questions/57542/adding-wireshark-xml-dictionary-and-wireshark-directory-structure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57542-score" class="post-score" title="current number of votes">0</div><span id="post-57542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have prepared the .xml file for diameter dictionary for Vendor specific AVP. It works on Windows-based Wireshark installation however under Red Hat I find the directory for adding the dictionary missing.</p><p>How I can solve the issue?</p><p>Directory /.wireshark :</p><pre><code>/# ls -a
.
..
cfilters
colorfilters
dictionary.xml
preferences
preferences_20141230
preferences_20150107
preferences_20150421
profiles
recent
recent_common</code></pre>// dictionary.xml is mine file and it doesn't work in main .wireshark location.</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-redhat" rel="tag" title="see questions tagged &#39;redhat&#39;">redhat</span> <span class="post-tag tag-link-dictionary" rel="tag" title="see questions tagged &#39;dictionary&#39;">dictionary</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '16, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/dc0f45fcee004be8c7ea3974ccdf0f33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82&#39;s gravatar image" /><p><span>Michał</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '16, 05:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-57542" class="comments-container"></div><div id="comment-tools-57542" class="comment-tools"></div><div class="clear"></div><div id="comment-57542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57546"></span>

<div id="answer-container-57546" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57546-score" class="post-score" title="current number of votes">1</div><span id="post-57546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's no user definable dictionary option at the moment. If you want to add AVP's you'll have to add them at the installed location, usually<code>/usr/share/wireshark/diameter</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '16, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57546" class="comments-container"></div><div id="comment-tools-57546" class="comment-tools"></div><div class="clear"></div><div id="comment-57546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

