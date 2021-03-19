+++
type = "question"
title = "Custom Dissector using an external library"
description = '''I have built a dissector in the windows os and everything works as planned. I have converted the dissector and the associated libraries to build on RHEL6. I have got it to the point where Wireshark is built and the plugin and everything else is built. When I run Wireshark I get the error message tha...'''
date = "2014-02-18T11:54:00Z"
lastmod = "2014-02-18T11:54:00Z"
weight = 29981
keywords = [ "error", "dll", "dissector", "undefined", ".so" ]
aliases = [ "/questions/29981" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Dissector using an external library](/questions/29981/custom-dissector-using-an-external-library)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29981-score" class="post-score" title="current number of votes">0</div><span id="post-29981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have built a dissector in the windows os and everything works as planned. I have converted the dissector and the associated libraries to build on RHEL6. I have got it to the point where Wireshark is built and the plugin and everything else is built. When I run Wireshark I get the error message that it "Couldn't load module /usr/local/lib/wireshark/plugins/1.11.2/mypluginname: undefined symbol functionname". The function that is in the error is in an external .so that I have built. I have checked the .so with the "nm -D" command and the function is in there. Where does Wireshark look for the external .so? Is it specified in one of the makefiles or what?<br />
</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-undefined" rel="tag" title="see questions tagged &#39;undefined&#39;">undefined</span> <span class="post-tag tag-link-.so" rel="tag" title="see questions tagged &#39;.so&#39;">.so</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '14, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/9856b06809a89fe6008d505da519be56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jk21&#39;s gravatar image" /><p><span>jk21</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jk21 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29981" class="comments-container"></div><div id="comment-tools-29981" class="comment-tools"></div><div class="clear"></div><div id="comment-29981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

