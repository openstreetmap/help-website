+++
type = "question"
title = "Push a new dissector to Wireshark"
description = '''My company, Control Techniques, has developed a dissector for the eCMP protocol that we use for factory communications. This dissector was developed by several employees, including myself. I used the GitExtensions application to clone the revision 1.11.4 source code, added our packet-ecmp.c source f...'''
date = "2014-05-04T16:49:00Z"
lastmod = "2014-05-06T16:33:00Z"
weight = 32513
keywords = [ "push", "dissector", "ecmp" ]
aliases = [ "/questions/32513" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Push a new dissector to Wireshark](/questions/32513/push-a-new-dissector-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32513-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My company, Control Techniques, has developed a dissector for the <strong>eCMP</strong> protocol that we use for factory communications. This dissector was developed by several employees, including myself.</p><p>I used the <strong>GitExtensions</strong> application to clone the revision 1.11.4 source code, added our <strong>packet-ecmp.c</strong> source file, and modified <strong>Makefile.common</strong> and <strong>CmakeLists.txt</strong> to add the name of our dissector source file. These changes built without error and the ecmp dissector works properly.</p><p>Is there any way to "push" these three files to Wireshark for inclusion in the built-in dissectors using the <strong>Git GUI</strong> or <strong>Git Extensions</strong> applications?</p><p>So far, I've had no luck with the current documentation which mostly shows examples using command line operations within a Git Bash shell.</p><p>Cheers, Jim Lynch Control Techniques</p></div><div id="question-tags" class="tags-container tags">push dissector ecmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '14, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/de90678c642298d64da5485408107dac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lynchzilla&#39;s gravatar image" /><p>lynchzilla<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lynchzilla has no accepted answers">0%</span></p></div></div><div id="comments-container-32513" class="comments-container"></div><div id="comment-tools-32513" class="comment-tools"></div><div class="clear"></div><div id="comment-32513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32521"></span>

<div id="answer-container-32521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32521-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know much about how the Wireshark devs work after moving to Git, but as far as I know they're using <a href="https://code.google.com/p/gerrit/">Gerrit</a>, which as far as I can tell works a bit different than standard Git requests.</p><p>Maybe you should subscribe to the developer mailing list directly and ask over there, if none of the devs sees and answers this question here: <a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">https://www.wireshark.org/mailman/listinfo/wireshark-dev</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '14, 20:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32521" class="comments-container"><span id="32526"></span><div id="comment-32526" class="comment"><div id="post-32526-score" class="comment-score">1</div><div class="comment-text"><p><a href="http://wiki.wireshark.org/Development/SubmittingPatches">http://wiki.wireshark.org/Development/SubmittingPatches</a></p></div><div id="comment-32526-info" class="comment-info"><span class="comment-age">(05 May '14, 00:24)</span> Anders ♦</div></div><span id="32544"></span><div id="comment-32544" class="comment"><div id="post-32544-score" class="comment-score">1</div><div class="comment-text"><p>Also note that for a new dissector, you should ideally create an entry in the <a href="http://bugs.wireshark.org">Wireshark Bugzilla</a> and attach at least one capture file to it. The captures added to Bugzilla are harvested for automated testing. Ensure you reference the Bugzilla entry correctly in the commit message with the "Bug: xxx" keyword.</p></div><div id="comment-32544-info" class="comment-info"><span class="comment-age">(06 May '14, 02:16)</span> grahamb ♦</div></div></div><div id="comment-tools-32521" class="comment-tools"></div><div class="clear"></div><div id="comment-32521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32572"></span>

<div id="answer-container-32572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32572-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per Anders's comment, the submission process is described in <a href="http://wiki.wireshark.org/Development/SubmittingPatches">the "Submitting Patches" page on the Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '14, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-32572" class="comments-container"></div><div id="comment-tools-32572" class="comment-tools"></div><div class="clear"></div><div id="comment-32572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

