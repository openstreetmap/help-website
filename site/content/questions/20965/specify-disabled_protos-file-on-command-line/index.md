+++
type = "question"
title = "specify disabled_protos file on command line"
description = '''How do I make tshark read a disabled_protos file (or any other config file) specified by name on the command line, rather than finding it in any of the stock locations? -C is the closest thing I&#x27;ve found to what I want, but that looks in ~/.wireshark/ for the profile directory, whereas I want to kee...'''
date = "2013-05-05T13:36:00Z"
lastmod = "2013-05-05T13:49:00Z"
weight = 20965
keywords = [ "tshark" ]
aliases = [ "/questions/20965" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [specify disabled\_protos file on command line](/questions/20965/specify-disabled_protos-file-on-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20965-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I make <code>tshark</code> read a <code>disabled_protos</code> file (or any other config file) specified by name on the command line, rather than finding it in any of the stock locations? <code>-C</code> is the closest thing I've found to what I want, but that looks in <code>~/.wireshark/</code> for the profile directory, whereas I want to keep my custom configuration files with the project they belong to.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '13, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/dd7cc06b1b1c347e172c6ba532937173?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zack&#39;s gravatar image" /><p>Zack<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zack has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '13, 13:36</p></div></div><div id="comments-container-20965" class="comments-container"></div><div id="comment-tools-20965" class="comment-tools"></div><div class="clear"></div><div id="comment-20965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20966"></span>

<div id="answer-container-20966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20966-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As there is no way to just point to a disabled_protocols file, you need to go the "-C" way. Here is one way of doing it:</p><p>Make a new profile for your project and then create a symbolic link to it in your projects directory:</p><pre><code>ln -s ~/.wireshark/profiles/projextX_profile_1 ~/projects/projectX/wireshark/profile_1</code></pre><p>Or if you want to keep the original files in your project directory, move the projectX_profile_1 directory to your projects directory and link back to it from ~/.wireshark/profiles</p><pre><code>mv ~/.wireshark/profiles/projextX_profile_1 ~/projects/projectX/wireshark/profile_1
ln -s ~/projects/projectX/wireshark/profile_1 ~/.wireshark/profiles/projextX_profile_1</code></pre><p>(FYI: I have linked my ~/.wireshark/profiles directory to a directory on dropbox so I have all my wireshark profiles available on both my laptops)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '13, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '13, 13:51</p></div></div><div id="comments-container-20966" class="comments-container"><span id="20967"></span><div id="comment-20967" class="comment"><div id="post-20967-score" class="comment-score"></div><div class="comment-text"><p>That's not a bad workaround, but it still requires me to set things up outside the project directory before my scripts will work. I want to be able to check out the repo in a pristine environment and proceed without further setup.</p></div><div id="comment-20967-info" class="comment-info"><span class="comment-age">(05 May '13, 13:52)</span> Zack</div></div><span id="20975"></span><div id="comment-20975" class="comment"><div id="post-20975-score" class="comment-score"></div><div class="comment-text"><p>The code for reading the profile name could be extended to also accept an absolute path. You could file an enhancement request for that on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> (or even better, provide the necessary patch so it can be submitted to the SVN repository)</p></div><div id="comment-20975-info" class="comment-info"><span class="comment-age">(06 May '13, 00:37)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-20966" class="comment-tools"></div><div class="clear"></div><div id="comment-20966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

