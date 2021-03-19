+++
type = "question"
title = "Temp file"
description = '''Hello -- I get the message when I start wireshark that it can&#x27;t write its temp file -- Where does it write it '''
date = "2012-01-03T11:22:00Z"
lastmod = "2012-01-04T03:52:00Z"
weight = 8205
keywords = [ "file", "temp" ]
aliases = [ "/questions/8205" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Temp file](/questions/8205/temp-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8205-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello -- I get the message when I start wireshark that it can't write its temp file -- Where does it write it</p></div><div id="question-tags" class="tags-container tags">file temp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '12, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/de69c90f0ed041938098e3285e627983?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fpefpe&#39;s gravatar image" /><p>fpefpe<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fpefpe has no accepted answers">0%</span></p></div></div><div id="comments-container-8205" class="comments-container"><span id="8214"></span><div id="comment-8214" class="comment"><div id="post-8214-score" class="comment-score"></div><div class="comment-text"><p>What is the <em>complete</em> message from Wireshark? It should be reporting <em>why</em> it can't write its temporary file.</p></div><div id="comment-8214-info" class="comment-info"><span class="comment-age">(03 Jan '12, 18:18)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8205" class="comment-tools"></div><div class="clear"></div><div id="comment-8205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8206"></span>

<div id="answer-container-8206" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8206-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>For windows it should be C:\Users\%Username%\AppData\Local\Temp</p><p>Open Wireshark and go to Help Menu then click on About Wireshark and from there choose the 3rd Tab which is Folders. Here you can find all the paths including Temp folder.</p><p>Goodluck,</p><p>A.G</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '12, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/559f374efd2eaeaafac5616bbec62008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminGho&#39;s gravatar image" /><p>AminGho<br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminGho has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jan '12, 13:37</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-8206" class="comments-container"><span id="8207"></span><div id="comment-8207" class="comment"><div id="post-8207-score" class="comment-score"></div><div class="comment-text"><p>hello --</p><p>Thx for the info -- can this be changed?</p></div><div id="comment-8207-info" class="comment-info"><span class="comment-age">(03 Jan '12, 11:43)</span> fpefpe</div></div><span id="8208"></span><div id="comment-8208" class="comment"><div id="post-8208-score" class="comment-score"></div><div class="comment-text"><p>I changed your answer to a comment. Wireshark writes into the temp folder specified in the environment variables, so if you change it Wireshark will write to the new location.</p></div><div id="comment-8208-info" class="comment-info"><span class="comment-age">(03 Jan '12, 13:36)</span> Jasper ♦♦</div></div></div><div id="comment-tools-8206" class="comment-tools"></div><div class="clear"></div><div id="comment-8206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8218"></span>

<div id="answer-container-8218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8218-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper said you can change the environment Variable and the temp folder will change Automatically but Personally I won't recommend this cuz it will cause other problems since there are lots of Applications which might use the Environment Variables and they might not function well sometimes. So instead create a new one and you know it won't affect the other apps. Here is how you do it :</p><p>Right click on My Computer &gt; Properties &gt; Advanced System Settings &gt; And go the the Advanced Tab &gt; Click on Environment Variables... Click New in the User Variables section and in the Variable Name Type TMPDIR and for the Variable Value specify any path which you would like to be your temp path like C:WShark_Temp</p><p>Now if you go back to About Wireshark and check the folders you will see that changes were made.</p><p>Also have in mind that if you have more than one user it's better to add it also in System Variables so you don't need to change it for each user separately.</p><p>Goodluck, A.G</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '12, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/559f374efd2eaeaafac5616bbec62008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminGho&#39;s gravatar image" /><p>AminGho<br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminGho has no accepted answers">0%</span></p></div></div><div id="comments-container-8218" class="comments-container"></div><div id="comment-tools-8218" class="comment-tools"></div><div class="clear"></div><div id="comment-8218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

