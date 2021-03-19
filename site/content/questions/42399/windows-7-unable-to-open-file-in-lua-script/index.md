+++
type = "question"
title = "[Windows 7] Unable to open file in Lua script"
description = '''I am trying to open a text file within my Lua script that is launched from Wireshark. However, it is not clear how to specify the filename as an absolute path or where the file should be stored. local csv_file = assert(io.open(&quot;AP_Batch.csv&quot;, &quot;r&quot;)) When this executes I get &quot;nil&quot; back. I tried the fo...'''
date = "2015-05-14T12:08:00Z"
lastmod = "2015-05-15T17:12:00Z"
weight = 42399
keywords = [ "lua", "windows7", "io.open" ]
aliases = [ "/questions/42399" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[Windows 7\] Unable to open file in Lua script](/questions/42399/windows-7-unable-to-open-file-in-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42399-score" class="post-score" title="current number of votes">0</div><span id="post-42399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to open a text file within my Lua script that is launched from Wireshark. However, it is not clear how to specify the filename as an absolute path or where the file should be stored.</p><p>local csv_file = assert(io.open("AP_Batch.csv", "r"))</p><p>When this executes I get "nil" back. I tried the following (with the same file copied into C:\temp)</p><p>local csv_file = assert(io.open("C:\Temp\AP_Batch.csv", "r"))</p><p>Where does Wireshark/Lua expect the current working directory to exist. I've copied the same file into Wireshark's installation folder, my home directory.</p><p>Could someone enlighten me what folder I should place the file or how to specify a full Windows style path.</p><p><strong>EDIT:</strong> I tried C:\\Temp\\AP_Batch.csv, but this failed. The error dialog tells me "No such file of directory" and displays c:\Temp\AP_Batch.csv as what it tried to open</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-io.open" rel="tag" title="see questions tagged &#39;io.open&#39;">io.open</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '15, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/8e191d3ad5ed97a4ab999dfe6087ae92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlwain74&#39;s gravatar image" /><p><span>carlwain74</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlwain74 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '15, 12:14</strong> </span></p></div></div><div id="comments-container-42399" class="comments-container"></div><div id="comment-tools-42399" class="comment-tools"></div><div class="clear"></div><div id="comment-42399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42401"></span>

<div id="answer-container-42401" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42401-score" class="post-score" title="current number of votes">0</div><span id="post-42401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some headway on this issue - File turned out to be named <strong>AP_Batch.csv.csv</strong> in Windows :-(</p><p>However, I would still like to know where Lua and Wireshark expect files to exist if no path is specified</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '15, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/8e191d3ad5ed97a4ab999dfe6087ae92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlwain74&#39;s gravatar image" /><p><span>carlwain74</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlwain74 has no accepted answers">0%</span></p></div></div><div id="comments-container-42401" class="comments-container"></div><div id="comment-tools-42401" class="comment-tools"></div><div class="clear"></div><div id="comment-42401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42406"></span>

<div id="answer-container-42406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42406-score" class="post-score" title="current number of votes">0</div><span id="post-42406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can refer this <a href="http://www.tutorialspoint.com/lua/lua_file_io.htm">lua file io</a></p><p>If no path is specified then io.open API bydefault takes that path where your .lua file is created for example if you have created sample.lua as below and you are trying to read test.lua from that</p><ol><li>--Opens a file in read</li><li>file = io.open("test.lua", "r")</li><li>-- sets the default input file as test.lua</li><li>io.input(file)</li><li>-- prints the first line of the file</li><li>print(io.read())</li></ol><p>then test.lua should be in that directory where your sample.lua is created and for the file which is in another directory you can define the path like io.open("D:\lua.txt,"r")</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '15, 21:15</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-42406" class="comments-container"><span id="42430"></span><div id="comment-42430" class="comment"><div id="post-42430-score" class="comment-score"></div><div class="comment-text"><p>ok sample.lua is located in the Wireshark folder. I confirmed that without a path it opens the file in this location.</p></div><div id="comment-42430-info" class="comment-info"><span class="comment-age">(15 May '15, 17:12)</span> <span class="comment-user userinfo">carlwain74</span></div></div></div><div id="comment-tools-42406" class="comment-tools"></div><div class="clear"></div><div id="comment-42406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

