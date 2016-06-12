This page provides documentation for some nonsense data. A few things to note in the `docs/example.yaml` file which defines the dataset features on this page:

1. **Datatype guesses** - Datadocs attempts to guess the datatype of each filed by reading the provided `.csv` file. If you want to ensure the proper datatypes is included, you can use the 'type' key when defining a field.
2. **Private fields** - The field `sex` is set to `private`. A private field is noted with a lock icon, and signals to the reader that while the field exists, it may not be available to be shared with others.
3. **Transformed fields** - The `is_male_likes_cake` is set to `transformed`. Transformation means the datapoint has some how been constructed. For example, in this case `is_male_likes_cake` is determined based on answers to the `Sex` and `Likes cake` fields. Transformed fields are noted by an "edit" icon.