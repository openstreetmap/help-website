+++
type = "question"
title = "Configuration Profile Confusion"
description = '''This is embarrassing, but does anyone else find setting and saving the Wireshark configuration profiles confusing? Here&#x27;s the use cases I&#x27;d like enumerated:  1) I have my columns set just the way I want them. I now want to save the setup as a configuration profile so I can reapply them later. This i...'''
date = "2013-12-16T13:05:00Z"
lastmod = "2013-12-16T13:21:00Z"
weight = 28180
keywords = [ "configuration" ]
aliases = [ "/questions/28180" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Configuration Profile Confusion](/questions/28180/configuration-profile-confusion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28180-score" class="post-score" title="current number of votes">0</div><span id="post-28180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is embarrassing, but does anyone else find setting and saving the Wireshark configuration profiles confusing?</p><p>Here's the use cases I'd like enumerated:</p><hr /><p>1) I have my columns set just the way I want them. I now want to save the setup as a configuration profile so I can reapply them later.</p><p>This is what I currently do:</p><ol><li>Under configuration profiles, hit new for a new profile.</li><li>Select the new profile and hit apply, assuming that it will apply the current configuration to that new profile.</li><li>Cry when it applies a different profile to the configuration that I painstakingly set up. (Was I supposed to hit ok instead?)</li></ol><hr /><p>2) I want my current configuration altered by the selected configuration profile.</p><p>This is what I currently do:</p><ol><li>Open up the configuration profiles.</li><li>Select the profile I'd like applied.</li><li>Hit OK.</li></ol><p>This seems to work. That is, it seems to apply the selected profile.</p><p>Obviously, I'm missing something subtle here. Does something make make the buttons OK and Apply do different things under different circumstances? Is there something about the order of the way I select the profile then hit apply that changes whether you're changing the profile or changing your current configuration?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '13, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/2e4763f0cc8124d677d249a99800950a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="firebush&#39;s gravatar image" /><p><span>firebush</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="firebush has no accepted answers">0%</span></p></div></div><div id="comments-container-28180" class="comments-container"></div><div id="comment-tools-28180" class="comment-tools"></div><div class="clear"></div><div id="comment-28180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28181"></span>

<div id="answer-container-28181" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28181-score" class="post-score" title="current number of votes">1</div><span id="post-28181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="firebush has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "New Profile" will create a new profile with default settings applied. So if you want to create a specific profile you should <strong>start</strong> by using "New Profile", then modify it. Not the other way around.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '13, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28181" class="comments-container"><span id="28182"></span><div id="comment-28182" class="comment"><div id="post-28182-score" class="comment-score"></div><div class="comment-text"><p>I see. So, if you realize you have things set up the way you want it and then decide to save it as a profile, there's no way to do so? You'll lose your setting when you create the new profile and it applies the default?</p></div><div id="comment-28182-info" class="comment-info"><span class="comment-age">(16 Dec '13, 13:13)</span> <span class="comment-user userinfo">firebush</span></div></div><span id="28183"></span><div id="comment-28183" class="comment"><div id="post-28183-score" class="comment-score">1</div><div class="comment-text"><p>Each profile except for the default profile is placed into a subdirectory of the "Personal Configuration" folder, while the default profile consists of the files found in the base "Personal configuration" folder. You can find the path of that folder if you take a look at the "Folders" tab of the "About Wireshark" dialog.</p><p>If you modified the settings of Wireshark you need to find the directory that contains the current profile. And then it's just a matter of copying/moving the files to another subfolder (which you can also create by hand if you want)</p></div><div id="comment-28183-info" class="comment-info"><span class="comment-age">(16 Dec '13, 13:17)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="28184"></span><div id="comment-28184" class="comment"><div id="post-28184-score" class="comment-score"></div><div class="comment-text"><p>Very good. Thanks for the input, Jasper!</p></div><div id="comment-28184-info" class="comment-info"><span class="comment-age">(16 Dec '13, 13:21)</span> <span class="comment-user userinfo">firebush</span></div></div></div><div id="comment-tools-28181" class="comment-tools"></div><div class="clear"></div><div id="comment-28181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

