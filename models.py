from django.db import models

class Article(models.Model):
  article_title = models.CharField('название статьи', max_length = 200)
  article_text = models.TextField('текст статьи')
  pub_date = models.DateTimeField('Дата публикации')

  def __str__(self):
    return self.article_title

    def was_published_recently(self):
      return self.pub_date >= (timezone() - datetime.timedelta(days = 7 ))

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete = models.CASCADE)
  author_name = models.CharField('имя автора', max_length =   100)
  comment_text = models.CharField('Текст комментария', max_length = 200)

  def __str__(self):
    return self.author_name
class Content(models.Model):
  content = models.CharField('иди нахрен', max_length =   100)