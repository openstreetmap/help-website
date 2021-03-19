+++
type = "question"
title = "How to modify the values of an enum preference after registering?"
description = '''Hello I would like to know whether it is possible to change the values of an enum preference after registering. I am integrating a tool to my custom dissector and this tool parses a specific file and extracts information. Based on the information extracted, the dissector should change/update the val...'''
date = "2016-12-15T06:58:00Z"
lastmod = "2016-12-15T06:58:00Z"
weight = 58138
keywords = [ "dissector", "preferences", "plugin" ]
aliases = [ "/questions/58138" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to modify the values of an enum preference after registering?](/questions/58138/how-to-modify-the-values-of-an-enum-preference-after-registering)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58138-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I would like to know whether it is possible to change the values of an enum preference after registering. I am integrating a tool to my custom dissector and this tool parses a specific file and extracts information. Based on the information extracted, the dissector should change/update the values of an enum preference so that the user will see an updated drop down box(with new options) in the preferences.</p><p>If it is not possible to change the enum values after registering a preference, is there some way to de-register/delete a previously registered preference and add a new preference?</p></div><div id="question-tags" class="tags-container tags">dissector preferences plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '16, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/70baba446202981a08e25a49438b4161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sherlock_000&#39;s gravatar image" /><p>sherlock_000<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sherlock_000 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '16, 06:59</p></div></div><div id="comments-container-58138" class="comments-container"><span id="58163"></span><div id="comment-58163" class="comment"><div id="post-58163-score" class="comment-score"></div><div class="comment-text"><p>I have managed to solve part of my question. I am now able to update the enum preference values after registering. The following is what I did:</p><ul><li><p>Created a fixed length array of type <code>enum_val_t</code> and initialized all entries to End of List value <code>(NULL for Name and Description and -1 for value)</code></p></li><li><p>Registered the enum preference using a reference to this array</p></li><li><p>Whenever the values of the enum preference drop-down list needs to be changed, I update the corresponding values to this array with an End of List entry at the last (I always make sure that the maximum entries within this array shall never go beyond its fixed length)</p></li></ul><p>I am not sure whether it is the right solution but it works for me!</p><p>However, there is still one problem for which I would like to hear some suggestions. Once the preference is registered, if there occurs a scenario where no are entries needed to be displayed in the enum list, I want to hide the preference from the user. But with my current approach, the preference will be visible to the user with no options to choose from the drop-down list.</p><p>So my question is, is temporary hiding of a preference possible? If not, is it atleast possible to delete a preference (so that I can register it again if needed)?</p></div><div id="comment-58163-info" class="comment-info"><span class="comment-age">(16 Dec '16, 03:43)</span> sherlock_000</div></div></div><div id="comment-tools-58138" class="comment-tools"></div><div class="clear"></div><div id="comment-58138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

