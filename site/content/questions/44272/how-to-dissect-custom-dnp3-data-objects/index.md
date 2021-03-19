+++
type = "question"
title = "How to dissect custom DNP3 data objects?"
description = '''Is there a way I can alter what the INFO tab displays. I am using a DNP3 protocol and trying to figure out what is going on. There is a custom DNP object that I would like to try to define and display in the &quot;Info&quot; column. I would like to post data from the DNP3 Applicaation Layer (One of the data o...'''
date = "2015-07-17T16:17:00Z"
lastmod = "2015-07-17T16:34:00Z"
weight = 44272
keywords = [ "info", "dnp", "dnp3" ]
aliases = [ "/questions/44272" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect custom DNP3 data objects?](/questions/44272/how-to-dissect-custom-dnp3-data-objects)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44272-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way I can alter what the INFO tab displays. I am using a DNP3 protocol and trying to figure out what is going on. There is a custom DNP object that I would like to try to define and display in the "Info" column. I would like to post data from the DNP3 Applicaation Layer (One of the data objects). I would like to take these data objects and display them directly in the info (obviously only if they exist).</p></div><div id="question-tags" class="tags-container tags">info dnp dnp3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '15, 16:17</strong></p><img src="https://secure.gravatar.com/avatar/b9e6d42de16d7fd42a75edf7470f0ebc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="napkinsterror&#39;s gravatar image" /><p>napkinsterror<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="napkinsterror has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '15, 17:24</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-44272" class="comments-container"></div><div id="comment-tools-44272" class="comment-tools"></div><div class="clear"></div><div id="comment-44272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44273"></span>

<div id="answer-container-44273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44273-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll probably need to modify the dissector to do that, or you might be able to do something with a Lua post-dissector or chained dissector, the difficulty with the lua approaches is getting access to the re-assembled application layer data.</p><p>There's no facilities at the moment for defining a custom data type for the dissector.</p><p>What's the custom object type you're trying to dissect? Can you post a capture in a public place, e.g. <a href="https://cloudshark.org">Cloudshark</a>, Google Drive, Dropbox etc.?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44273" class="comments-container"><span id="44276"></span><div id="comment-44276" class="comment"><div id="post-44276-score" class="comment-score"></div><div class="comment-text"><p>I have just left my office. I will post it when I get home. It's an official DNP object called an 8-bit unsigned integer object . It allows you to customize the object further as it is just a generic byte. Just like binary and analog values this has a type called Object 102 in the DNP Spec. (Object Type is 0x6601).</p><p>I was able to open the application layer C code and find the variables and add this object. I was hoping to not have to write code as I am simply an intern and have never written code for wireshark but it seems as it might be necessary here. The difficulty will be converting the bytes (application layer object's data) into ASCII bytes and adding that to the column info without breaking wireshark. I will look into LUA but if it's hard to get the data from the application later then it won't be much help. That's the sole purpose I am doing this.</p><p>I also haven't figured out how to or where best to customize the info column based on the qualifier code and object header data.</p></div><div id="comment-44276-info" class="comment-info"><span class="comment-age">(17 Jul '15, 17:22)</span> napkinsterror</div></div><span id="44278"></span><div id="comment-44278" class="comment"><div id="post-44278-score" class="comment-score"></div><div class="comment-text"><p>So it's not a custom (user-defined) object, but one that isn't yet dissected. Generally I only add objects to the dissector when captures for those objects are available so I can test the new dissection.</p><p>Please raise an entry (marking it as an enhancement) on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>, attach a capture with the object of interest in it and post a link to the request back here as a comment.</p></div><div id="comment-44278-info" class="comment-info"><span class="comment-age">(18 Jul '15, 00:50)</span> grahamb ♦</div></div></div><div id="comment-tools-44273" class="comment-tools"></div><div class="clear"></div><div id="comment-44273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

