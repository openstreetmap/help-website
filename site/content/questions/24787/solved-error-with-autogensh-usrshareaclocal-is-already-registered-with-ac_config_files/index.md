+++
type = "question"
title = "[SOLVED] Error with &quot;autogen.sh&quot; - /usr/share/aclocal &#x27; is already registered with AC_CONFIG_FILES"
description = '''Hi all, I&#x27;m trying to build Wireshark for Linux version but I cannot start with the script &quot;autogen.sh&quot;. I have already installed autoconf, automake, lib-tool to fix some errors but it shows another as shown in the figure below  And the output of &quot;sh -x ./autogen.sh&quot; is   It seems that there is a pr...'''
date = "2013-09-16T18:53:00Z"
lastmod = "2013-09-17T18:16:00Z"
weight = 24787
keywords = [ "ac_config_files", "autogen.sh" ]
aliases = [ "/questions/24787" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[SOLVED\] Error with "autogen.sh" - /usr/share/aclocal ' is already registered with AC\_CONFIG\_FILES](/questions/24787/solved-error-with-autogensh-usrshareaclocal-is-already-registered-with-ac_config_files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24787-score" class="post-score" title="current number of votes">0</div><span id="post-24787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm trying to build Wireshark for Linux version but I cannot start with the script "autogen.sh". I have already installed autoconf, automake, lib-tool to fix some errors but it shows another as shown in the figure below</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2013-09-17_08:43:39.png" alt="alt text" /></p><p>And the output of "sh -x ./autogen.sh" is</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2013-09-17_08:48:05.png" alt="alt text" /></p><p>It seems that there is a problem with AC_CONFIG_FILES but I don't know how to fix. Please help me if you have any idea or suggestion. Thank you so much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ac_config_files" rel="tag" title="see questions tagged &#39;ac_config_files&#39;">ac_config_files</span> <span class="post-tag tag-link-autogen.sh" rel="tag" title="see questions tagged &#39;autogen.sh&#39;">autogen.sh</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '13, 02:56</strong> </span></p></div></div><div id="comments-container-24787" class="comments-container"><span id="24788"></span><div id="comment-24788" class="comment"><div id="post-24788-score" class="comment-score"></div><div class="comment-text"><p>Btw, I'm using Ubuntu, the latest version.</p></div><div id="comment-24788-info" class="comment-info"><span class="comment-age">(16 Sep '13, 18:57)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-24787" class="comment-tools"></div><div class="clear"></div><div id="comment-24787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24789"></span>

<div id="answer-container-24789" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24789-score" class="post-score" title="current number of votes">0</div><span id="post-24789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi all, problem solved. Most of problem caused by the EOL "^M" in the script, so you should re-write those files including: autogen, configure.ac, aclocal-flags by using this command:</p><ul><li>$cp configure.ac configure.ac.bak</li><li>$tr -d '\r' &lt;configure.ac.bak&gt;configure.ac</li></ul><p>So I will not delete this question in order to help other developers if they have the same problem. Thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></img></div></div><div id="comments-container-24789" class="comments-container"><span id="24816"></span><div id="comment-24816" class="comment"><div id="post-24816-score" class="comment-score">1</div><div class="comment-text"><p>You might have ^M's in that (and other) scripts if you checked out the source code using a Windows SVN client. The scripts have the SVN property eol-style set to "native."</p></div><div id="comment-24816-info" class="comment-info"><span class="comment-age">(17 Sep '13, 06:08)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="24869"></span><div id="comment-24869" class="comment"><div id="post-24869-score" class="comment-score"></div><div class="comment-text"><p>Yes. There are <em>no</em> ^Ms in the file if you check it out on a UN*X, but there will be ^Ms in the file if you check it out on Windows.</p></div><div id="comment-24869-info" class="comment-info"><span class="comment-age">(17 Sep '13, 14:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24872"></span><div id="comment-24872" class="comment"><div id="post-24872-score" class="comment-score"></div><div class="comment-text"><p>Yes, you are right. Thanks for your comments. Now, my code is running successfully, thanks for your help</p></div><div id="comment-24872-info" class="comment-info"><span class="comment-age">(17 Sep '13, 18:16)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-24789" class="comment-tools"></div><div class="clear"></div><div id="comment-24789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

